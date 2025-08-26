import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

def get_llm():
    llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    return llm
