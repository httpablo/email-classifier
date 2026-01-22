import json

from app.core.config import OPENAI_MODEL_NAME, client



def analyze_email(text: str):
    system_prompt = """
    Você é uma IA assistente corporativa.
    Sua tarefa é analisar o email recebido e retornar um JSON com a estrutura abaixo:
    {
        "classification": "Produtivo" ou "Improdutivo",
        "confidence": <float entre 0.0 e 1.0>,
        "suggested_response": "<texto formatado do email>"
    }

    CATEGORIAS DE CLASSIFICAÇÃO:
    1. Produtivo: Solicitações de suporte, dúvidas, reclamações, orçamentos ou ações que exigem intervenção humana.
    2. Improdutivo: Agradecimentos ("Obrigado"), Felicitações ("Feliz Natal"), SPAM ou mensagens meramente informativas sem necessidade de ação.

    REGRAS DE RESPOSTA 'suggested_response':
    - A resposta DEVE seguir estritamente o formato de email corporativo:
      Assunto: [Assunto Sugerido]

      [Saudação adequada],

      [Corpo do email com parágrafos bem definidos]

      Atenciosamente,

    - Se 'Produtivo': Seja resolutivo, empático e profissional. Se faltarem dados, solicite-os polidamente. Use placeholders entre colchetes como [Nome do Cliente] ou [Data] se necessário.
    - Se 'Improdutivo': Agradeça o contato de forma breve e educada, encerrando o ciclo de conversa com estrtura de email.
    - Idioma: Português (Brasil).
    - Evite alucinações: Não invente números de protocolo ou datas que não existam no texto original.
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
