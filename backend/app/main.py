import time
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from .services.text import extract_text_from_pdf, preprocess_text
from .schemas import AnalysisResponse
from .services.ai import analyze_email

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://email-classifier-pablo.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(
    "/analyze",
    response_model=AnalysisResponse,
    summary="Analisa e Classifica Emails",
    description="Api recebe um texto ou arquivo PDF/TXT, aplica pré-processamento NLP e utiliza IA para classificar entre 'Produtivo' ou 'Improdutivo'",
)
async def analyze_email_endpoint(
    text_input: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    start_time = time.time()
    content = ""

    if text_input:
        content = text_input
    elif file:
        if file.filename.endswith(".pdf"):
            file_bytes = await file.read()
            content = extract_text_from_pdf(file_bytes)
        elif file.filename.endswith(".txt"):
            content = (await file.read()).decode("utf-8")
        else:
            raise HTTPException(status_code=400, detail="Formato não suportado. Use PDF ou TXT.")

    if not content.strip():
        raise HTTPException(status_code=400, detail="Não foi possível extrair texto do arquivo.")

    cleaned_content = preprocess_text(content)
    ai_result = await analyze_email(cleaned_content)

    end_time = time.time()
    process_time = round(end_time - start_time, 2)

    return {
        "original_text": content,
        "cleaned_text": cleaned_content,
        "classification": ai_result.get("classification"),
        "suggested_response": ai_result.get("suggested_response"),
        "process_time": f"{process_time}",
    }
