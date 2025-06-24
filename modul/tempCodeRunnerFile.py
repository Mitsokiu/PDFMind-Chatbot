if __name__ == "__main__":
    db = load_db("all-MiniLM-L6-v2-bf16-q4_k.gguf")
    query = "g. Một chai rượu vang có thể được định giá dựa  trên  yếu tố nào?"
    result = query_rag(db, query)
    print(">> Kết quả truy vấn:\n", result)
