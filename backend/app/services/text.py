import io
import string
import nltk
from pypdf import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.data.find('tokenizers/punkt_tab')
nltk.data.find('corpora/stopwords')


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        pdf_reader = PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    except Exception as e:
        print(f"Erro ao ler PDF: {e}")
        return ""


def preprocess_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text, language='portuguese')
    stop_words = set(stopwords.words('portuguese'))

    cleaned_tokens = []
    for word in tokens:
        if word not in stop_words:
            cleaned_tokens.append(word)

    return " ".join(cleaned_tokens)
