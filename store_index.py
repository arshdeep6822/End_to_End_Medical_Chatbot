from src.medical_chatbot.helper import load_pdf, text_split, downloading_embeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV_KEY = os.environ.get('PINECONE_ENV_KEY')

#print(PINECONE_ENV_KEY)
#print(PINECONE_API_KEY)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embedding_model = downloading_embeddings()

pc = Pinecone(
    api_key = PINECONE_API_KEY,  # Ensure your API key is set in the environment
    environment = PINECONE_ENV_KEY
)

index_name = 'mchatbot'
index = pc.Index(index_name)

vector_store = PineconeVectorStore(index=index, embedding=embedding_model)
from uuid import uuid4
documents_with_ids = [{'id': str(uuid4()), 'text': chunk.page_content} for chunk in text_chunks]
uuids = []
for doc in documents_with_ids:
    uuids.append(doc.get('id'))
vector_store.add_documents(documents=text_chunks, id=uuids)

