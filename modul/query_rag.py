from langchain.vectorstores import FAISS
from langchain_community.embeddings import GPT4AllEmbeddings

def load_db(model_path, db_path="vectordb"):
    embedder = GPT4AllEmbeddings(model_path=model_path)
    db = FAISS.load_local(db_path, embedder, allow_dangerous_deserialization=True)
    return db

def query_rag(db, query, k=3):
    docs = db.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context
