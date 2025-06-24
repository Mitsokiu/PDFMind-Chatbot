# PDFMind-chatbot
PDFMind is a chatbot that reads and understands PDF documents using a local large language model (LLM) combined with Retrieval-Augmented Generation (RAG). Users can upload PDF files and ask questions, receiving answers based on the document content.

## Features

- Extracts and processes content from PDF files in the `data/` folder
- Splits text into manageable chunks
- Embeds and stores vector representations using FAISS
- Retrieves relevant context and generates answers using a local LLM (Vinallama)
- Simple web interface for chatting and file uploading


## Technologies Used

- Python 3.10+
- LangChain
- GPT4All Embeddings
+ link model embedding  : https://huggingface.co/mlx-community/all-MiniLM-L6-v2-bf16
- FAISS (vector search)
- FastAPI (backend API)
- Vinallama (.gguf local language model)  :
+link model : https://huggingface.co/vilm/vinallama-7b-chat
- Vanilla HTML/CSS/JavaScript (frontend)



