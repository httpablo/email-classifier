# 📨 Email Classifier

![React](https://img.shields.io/badge/Frontend-React%20%2B%20Vite-blue?style=for-the-badge&logo=react)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT--4-412991?style=for-the-badge&logo=openai)
![Docker](https://img.shields.io/badge/Infra-Docker-2496ED?style=for-the-badge&logo=docker)

> Uma solução inteligente de classificação automática de emails que utiliza inteligência artificial para determinar se um email necessita de resposta e gerar respostas apropriadas quando necessário.

---

## 🎯 Sobre o Projeto

No cenário financeiro atual, o volume de emails pode sobrecarregar as equipes de atendimento. O **Email Classifier** foi projetado para resolver esse problema automatizando a primeira camada de triagem.

A aplicação lê o conteúdo de emails (seja via texto direto ou upload de arquivos PDF/TXT), utiliza Inteligência Artificial para entender o contexto e realiza duas ações principais:

1.  **Classificação:** Define se o email é **Produtivo** (requer ação da equipe) ou **Improdutivo** (apenas informativo/agradecimento).
2.  **Sugestão de Resposta:** Redige automaticamente uma minuta de resposta contextualizada e polida, pronta para ser enviada.

### ✨ Funcionalidades Principais

- **Análise Inteligente:** Compreensão semântica do texto.
- **Upload Flexível:** Suporte nativo para arquivos `.txt` e `.pdf`.
- **Respostas Contextuais:** A IA gera respostas que variam o tom em agradecimento ou suporte técnico.

---

## 🚀 Como Funciona o Fluxo

```
1. 📝 Usuário insere email (texto, PDF ou TXT)
     ↓
2. 🔄 Backend extrai e limpa o texto (NLP)
     ↓
3. 🧠 IA analisa o contexto
     ↓
4. 🎯 Classifica (Produtivo vs. Improdutivo)
     ↓
5. ✍️ Redige a sugestão de resposta ideal
```

---

## 🛠️ Decisões Técnicas e Tecnologias

Para atender aos requisitos de **Qualidade Técnica** e **Uso de AI**, a arquitetura foi pensada para ser escalável e de fácil manutenção.

### 🧠 Inteligência Artificial (Backend)

Optou-se pelo uso da API da **OpenAI (modelo GPT-4o-mini)**.

- **GPT-4o-mini:** Oferece uma latência extremamente baixa com uma capacidade de raciocínio superior para contextos nuances (sarcasmo, urgência) que modelos locais menores poderiam perder, além de não sobrecarregar a infraestrutura de deploy.
- **Engenharia de Prompt:** O sistema utiliza prompts estruturados para garantir que a resposta saia sempre em formato JSON estrito, facilitando o parsing pelo Frontend.

### 💻 Interface (Frontend)

Desenvolvida com **React** e **TypeScript** utilizando **Vite**.

- O design utiliza **Tailwind CSS** para garantir responsividade e uma estética profissional e limpa, focada na usabilidade do operador.
- Implementação de feedback de carregamento e tratamento de erros de conexão.

### 🐳 Infraestrutura (Docker)

A aplicação foi totalmente containerizada utilizando Docker e Docker Compose.

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Docker e Docker Compose instalados.
- Uma chave de API da OpenAI.

### Passo a Passo

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/SEU-USUARIO/email-classifier.git](https://github.com/SEU-USUARIO/email-classifier.git)
    cd email-classifier
    ```

2.  **Configure as Variáveis de Ambiente:**
    Na pasta `backend`, crie um arquivo `.env` (baseado no `.env.example` se houver) e adicione sua chave:

    ```env
    OPENAI_API_KEY=sua-chave-aqui-sk-...
    OPENAI_MODEL_NAME=gpt-4o-mini
    ```

3.  **Inicie a Aplicação:**
    Na raiz do projeto, execute:

    ```bash
    docker compose up --build
    ```

4.  **Acesse:**
    - **Frontend:** `http://localhost:5173`
    - **Documentação da API (Swagger):** `http://localhost:8000/docs`

---

## 🧪 Dados para Teste

Disponibilizei uma pasta chamada `/data` na raiz deste repositório contendo emails fictícios para teste:

- 📂 **Produtivos:** Exemplos de solicitações de suporte e envio de comprovantes.
- 📂 **Improdutivos:** Exemplos de mensagens de boas festas e agradecimentos simples.

Sinta-se à vontade para arrastar esses arquivos para a área de upload da aplicação.

---

## 📂 Estrutura do Repositório

Organizamos o código seguindo o padrão de monorepo para clareza:

```text
email-classifier/
├── backend/                # API FastAPI
│   ├── app/
│   │   ├── services/       # Lógica de IA e Processamento de Texto
│   │   └── main.py         # Endpoints e Configuração
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/               # Interface React
│   ├── src/components/     # Componentes de UI (Cards, Inputs)
│   ├── Dockerfile
│   └── ...
├── data/                   # Arquivos de exemplo (.txt e .pdf) para teste
└── docker-compose.yml      # Orquestração dos containers
```
