from flask import Flask, render_template, jsonify, request
from src.medical_chatbot.helper import downloading_embeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.medical_chatbot.prompt import *
import os

app = Flask(__name__)

load_dotenv()

# loading the vector store
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENV_KEY = os.environ.get('PINECONE_ENV_KEY')
embedding_model = downloading_embeddings()
pc = Pinecone(
    api_key = PINECONE_API_KEY,  # Ensure your API key is set in the environment
    environment = PINECONE_ENV_KEY
)
index_name = 'mchatbot'
vector_store = PineconeVectorStore.from_existing_index(index_name, embedding_model)

PROMPT = PromptTemplate(
    input_variables=["context","question"],
    template=prompt_template
)

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
llm = OpenAI(api_key=OPENAI_API_KEY)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={'prompt': PROMPT}
)

@app.route("/")
def index():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)
