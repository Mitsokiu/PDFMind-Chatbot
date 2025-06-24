def build_prompt(context, question):
    prompt = f"""
Bạn là một trợ lý AI chuyên đọc hiểu tài liệu. Hãy trả lời ngắn gọn và chính xác dựa trên nội dung sau:

### Tài liệu:
{context}

### Câu hỏi:
{question}

### Trả lời:
"""
    return prompt


from llama_cpp import Llama

llm = Llama(model_path="model/vinallama-7b-chat_q5_0.gguf", n_ctx=2048)

def ask_vina(prompt):
    output = llm(prompt, max_tokens=300, stop=["###"])
    return output["choices"][0]["text"].strip()
