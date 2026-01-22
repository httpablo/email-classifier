import json

from app.core.config import OPENAI_MODEL_NAME, client


async def analyze_email(text: str):
    system_prompt = """
    Sua única tarefa é analisar o e-mail abaixo e retornar um JSON. Não adicione nenhum texto extra.

    O formato de saída deve ser um JSON válido com a estrutura abaixo:
    {
        "classification": "Produtivo" ou "Improdutivo",
        "suggested_response": "<texto formatado do email>"
    }

    - "categoria": Classifique como "Produtivo" APENAS se o e-mail exigir uma ação concreta, resposta ou trabalho. Caso contrário, classifique como "Improdutivo". E-mails de agradecimento, felicitações, avisos ou SPAM são Improdutivos.

    -----------------------------------------------------------------------
    Todas as sugestões de resposta DEVEM seguir estritamente este template:
    Prezado(a),

    [Corpo da resposta curto e contextual]

    Atenciosamente,
    [Seu Nome]
    -----------------------------------------------------------------------

    - "sugestao_resposta": Sugira uma resposta curta, profissional e contextual.
      - Para e-mails Produtivos, a resposta deve confirmar o recebimento e indicar o próximo passo.
      - Para e-mails Improdutivos, a resposta deve ser adaptada ao conteúdo:
        - Se for um agradecimento, responda com gentileza (ex: "Ficamos felizes em ajudar!").
        - Se for uma felicitação (aniversário, festas), retribua os votos (ex: "Agradecemos e desejamos o mesmo a você!").
        - Se for um aviso ou comunicado, apenas confirme o recebimento (ex: "Obrigado pelo aviso.").
        - Se for um simples "ok" ou "recebido", a resposta pode ser "Confirmado, obrigado.".

    A seguir, exemplos de como você deve se comportar.

    **Exemplo 1 (Produtivo - Pedido de Suporte):**
    {{
      "classification": "Produtivo",
      "suggested_response": "Olá. Recebemos sua solicitação e nossa equipe já está analisando o problema. Retornaremos assim que tivermos uma atualização."
    }}

    **Exemplo 2 (Improdutivo - Agradecimento):**
    {{
      "classification": "Improdutivo",
      "suggested_response": "De nada! Ficamos felizes em ajudar. Tenha um ótimo dia."
    }}

    **Exemplo 3 (Improdutivo - Aviso):**
    {{
      "classification": "Improdutivo",
      "suggested_response": "Ciente. Agradecemos pelo comunicado."
    }}
    """

    try:
        response = await client.chat.completions.create(
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
            "suggested_response": "Não foi possível processar este email no momento."
        }
