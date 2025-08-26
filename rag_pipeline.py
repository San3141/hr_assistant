from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
load_dotenv()
def load_vector_store():
    # file_path = 'C:/Users/sanja/OneDrive/Desktop/hr_assistant/HR Policies.pdf'
    # loader = PyPDFLoader(file_path)
    # doc = data = loader.load()
    # # embeddings
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # splitter  = RecursiveCharacterTextSplitter(
    #     chunk_size=800,
    #     chunk_overlap=100,
    #     is_separator_regex=False,
    # )

    # texts = splitter.split_documents(doc)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
        persist_directory="./chroma_langchain_db",
    )
    return vector_store

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_chroma import Chroma
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Initialize embedding model once
# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# def load_and_split(file_path: str):
#     """Load a PDF and split it into chunks"""
#     loader = PyPDFLoader(file_path)
#     docs = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100,
#         is_separator_regex=False,
#     )
#     return splitter.split_documents(docs)

# def build_vectorestore(texts=None):
#     """Create or load a Chroma vector store"""
#     vector_store = Chroma(
#         collection_name="example_collection",
#         embedding_function=embeddings,
#         persist_directory="./chroma_langchain_db",
#     )

#     if texts:  # Only add documents if explicitly provided
#         vector_store.add_documents(documents=texts)
#         vector_store.persist()  # Save to disk so it’s reusable

#     return vector_store
