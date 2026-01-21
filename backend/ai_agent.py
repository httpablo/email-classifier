import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")


def analyze_email(text: str):
    system_prompt = """
    Você é uma IA assistente corporativa especializada em triagem de emails.
    Sua tarefa é analisar o email recebido e retornar um JSON estritamente com a seguinte estrutura:
    {
        "classification": "Produtivo" ou "Improdutivo",
        "confidence": <float entre 0 e 1 indicando certeza>,
        "suggested_response": "<texto da resposta sugerida>"
    }

    CATEGORIAS DE CLASSIFICAÇÃO:
    - Produtivo: Emails que exigem ação, suporte, dúvidas técnicas, cobranças ou agendamentos.
    - Improdutivo: Agradecimentos simples, felicitações (Natal, Aniversário), SPAM ou mensagens que não exigem resposta.

    REGRAS DE RESPOSTA:
    - Se Produtivo: Escreva uma resposta formal, empática e direta abordando o problema.
    - Se Improdutivo: Escreva uma resposta curta e educada de agradecimento.
    - O idioma da resposta deve ser Português (Brasil).
    """

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Email recebido:\n{text}"}
            ],
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        result = json.loads(content)

        return result

    except Exception as e:
        print(f"Erro na OpenAI: {e}")
        return {
            "classification": "Erro",
            "confidence": 0.0,
            "suggested_response": "Não foi possível processar este email no momento."
        }
