from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from embeddings import embeddings, text_splitter
from dotenv import load_dotenv

load_dotenv()
embeddings= embeddings()
texts = text_splitter()
def build_vectorestore():
    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",
    )
    vector_store.add_documents(documents=texts)

    return vector_store

