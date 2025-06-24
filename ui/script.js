async function uploadPDF() {
  const fileInput = document.getElementById("pdf-file");
  const file = fileInput.files[0];

  if (!file || file.type !== "application/pdf") {
    alert("Vui lòng chọn đúng định dạng PDF.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    alert("✅ Tải lên thành công: " + data.filename);
  } catch (err) {
    alert("❌ Lỗi khi tải lên: " + err.message);
  }
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();
  if (!message) return;

  // Hiển thị tin nhắn người dùng
  const userMsg = document.createElement("div");
  userMsg.className = "chat-message user";
  userMsg.textContent = message;
  chatBox.appendChild(userMsg);
  chatBox.scrollTop = chatBox.scrollHeight;
  input.value = "";

  // Gửi API
  try {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: message })
    });
    const data = await res.json();

    const botMsg = document.createElement("div");
    botMsg.className = "chat-message bot";
    botMsg.textContent = data.answer;
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    const botMsg = document.createElement("div");
    botMsg.className = "chat-message bot";
    botMsg.textContent = "⚠️ Lỗi kết nối: " + err.message;
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
}
