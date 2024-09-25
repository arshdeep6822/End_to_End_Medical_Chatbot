prompt_template = """
    use the following pieces of information to answer the user's question.
    if you dont know the answer, just say that you dont know the answer, dont try to make up an answer.
    
    Context:{context}
    Question: {question}
    
    Only return the helpful answer below and nothin else
    Helpful answer:
    """