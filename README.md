# AI-Powered Log Analysis Portal 🤖📊

This is a lightweight, local AI tool built to help engineers quickly analyze, summarize, and interact with log files using LLMs.

---

## 🔍 About the Project

Dealing with raw log files is time-consuming and tedious. This AI-powered Log Analysis Portal reads log content and lets users ask natural-language questions about it, providing concise summaries or insights in real time.

---

## ✅ Features

📂 Upload support for `.txt`, `.log`, and `.pcap` files  
🧠 Uses **LLaMA 3.2** (via **Ollama**) for local LLM-powered summarization  
💬 Ask questions about logs and receive smart answers instantly  
⚡ Powered by multi-threading for responsive performance  
🖥️ Built with Streamlit for a fast, interactive browser-based UI  
🔐 No cloud dependencies – runs completely offline  

---

## 🧰 Tech Stack

- Python  
- Streamlit  
- [Ollama](https://ollama.com) (for running `llama3.2`)  
- SentenceTransformers  
- PyShark, Chardet, Pillow (file handling and detection)  
- Subprocess/threading for efficient background processing  

---

## 📦 Setup Instructions

### 1. Install Ollama and pull the LLaMA model

```bash
ollama pull llama3.2
```

### 2. Clone this repository

```bash
git clone https://github.com/rajeshbakthavachalam/log-analysis-portal
cd log-analysis-portal
```

### 3. Create and activate your Python environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📎 Example Use Cases

- Summarize security or performance logs  
- Troubleshoot large logs by asking targeted questions  
- Understand patterns or errors without manually searching  
- Use in test, dev, or production environments  

---

## 🛠️ Planned Improvements

- Grouped summaries (by timestamp, severity, module)  
- Smart anomaly detection  
- Vector DB integration for multi-file search  
- Support for charts (log frequency, types, etc.)  
- Multi-model support (DeepSeek, Claude, Mistral, etc.)  

---

## 🤝 Contributions & Feedback

This is an open proof-of-concept project. Contributions, issues, and suggestions are welcome!

---

## 📄 License

MIT License

---

Let’s make log analysis simpler, smarter, and faster with AI. 💡
