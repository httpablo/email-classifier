import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
