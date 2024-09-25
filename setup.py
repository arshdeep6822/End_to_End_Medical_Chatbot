#installing src as our local package

from setuptools import find_packages, setup

setup(
    name='medical_chatbot',
    version='0.0.0',
    author='Arshdeep Singh',
    author_email='deeparsh618@gmail.com',
    packages=find_packages(),
    install_requires=["ctransformers",
                      "pinecone-client","langchain","flask",
                      "pypdf","langchain_pinecone","langchain-community","langchain-huggingface","transformers","openai","tiktoken"]
)