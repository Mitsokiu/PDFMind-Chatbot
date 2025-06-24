from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil, os

from modul.query_rag import load_db, query_rag
from modul.vinallm import build_prompt, ask_vina
from vectordb.build_vector_db import build_vector_store

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()

# Cho phép frontend gọi từ bất kỳ origin nào (dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tải vectorDB và mô hình
db = load_db("model/all-MiniLM-L6-v2-bf16-q4_k.gguf", db_path="vectordb")

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return JSONResponse({"error": "File không phải PDF"}, status_code=400)
    
    save_path = f"uploaded_files/{file.filename}"
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    build_vector_store("uploaded_files", "model/all-MiniLM-L6-v2-bf16-q4_k.gguf", "vectordb")

    return {"filename": file.filename}

@app.post("/ask")
async def ask_api(req: Request):
    body = await req.json()
    query = body.get("question", "")
    if not query:
        return JSONResponse({"error": "Thiếu câu hỏi"}, status_code=400)
    
    context = query_rag(db, query, k=3)
    prompt = build_prompt(context, query)
    answer = ask_vina(prompt)

    return {"answer": answer}


app.mount("/static", StaticFiles(directory="ui"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open("ui/index.html", "r", encoding="utf-8") as f:
        return f.read()