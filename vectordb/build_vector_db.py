from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.vectorstores import FAISS

def build_vector_store(pdf_dir, model_path, db_path):
    loader = DirectoryLoader(
        pdf_dir,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embedder = GPT4AllEmbeddings(model_path=model_path)
    db = FAISS.from_documents(chunks, embedder)
    db.save_local(db_path)
    print(f"Saved vector DB to: {db_path} | Tổng số đoạn: {len(chunks)}")

