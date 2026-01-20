from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Backend is running!"}

@app.post("/analyze")
async def analyze_email_endpoint(
    text_input: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    content = ""
    
    if text_input:
        content = text_input
    elif file:
        if file.filename.endswith(".pdf"):
            pass
        elif file.filename.endswith(".txt"):
            content = (await file.read()).decode("utf-8")
        else:
            raise HTTPException(status_code=400, detail="Formato não suportado")
    
    if not content:
        raise HTTPException(status_code=400, detail="Nenhum conteúdo fornecido")
    
    
    return {
        "original_text": content[:100] + "...",
        "classification": "Produtivo",
        "confidence": 0.95,
        "suggested_response": "Prezado cliente, recebemos sua solicitação e..."
    }
