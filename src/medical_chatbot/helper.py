from langchain.document_loaders import PyPDFLoader, PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
import os


def load_pdf(data):
    loader = DirectoryLoader(
        data,
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    
    documents = loader.load()
    return documents


def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    
    return text_chunks

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
def downloading_embeddings():
    embedding_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    return embedding_model