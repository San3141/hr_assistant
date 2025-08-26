from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = 'C:/Users/sanja/OneDrive/Desktop/hr_assistant/HR Policies.pdf'

loader = PyPDFLoader(file_path)
doc = data = loader.load()

def embeddings():
    # embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embeddings

def text_splitter():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        is_separator_regex=False,
    )
    texts = text_splitter.split_documents(doc)
    return texts