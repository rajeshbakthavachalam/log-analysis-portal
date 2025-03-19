import streamlit as st
import subprocess
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import threading
import chardet  # Ensure chardet is imported
from PIL import Image

# Set up page configuration and styling
st.set_page_config(page_title="Log Analysis Portal", page_icon="🤖", layout="wide")

# Load and display a banner image
st.image("https://raw.githubusercontent.com/your-repo/banner.png", use_column_width=True)

# Constants
MAX_FILE_SIZE = 200 * 1024 * 1024
OLLAMA_PATH = "C:\\Users\\rajes\\AppData\\Local\\Programs\\Ollama\\ollama.exe"  # Adjusted for Windows
MODEL_NAME = "llama3.2:latest"  # Switched to LLaMA 3.2
embedder = SentenceTransformer('all-MiniLM-L6-v2', device="cpu")

# Sidebar for navigation
st.sidebar.title("Navigation 🧭")
st.sidebar.markdown("[GitHub Repo](https://github.com/rajeshbakthavachalam/log-analysis-portal/) | [LinkedIn](https://www.linkedin.com/in/rajesh-b-a120a824/)")
st.sidebar.info("Upload logs, ask questions, and analyze logs efficiently.")

# Function to run LLaMA 3.2 query
def ask_llama(question, context=""):
    input_text = f"Task: Summarize the following log file.\n\nLog Content:\n{context[:1500]}\n\nSummary:"
    try:
        result = subprocess.run(
            [OLLAMA_PATH, "run", MODEL_NAME],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=600,  # Increased timeout
            encoding="utf-8",
            errors="replace"
        )
        if result.returncode != 0:
            if "Access is denied" in result.stderr:
                return "⚠️ Permission Error: Please run the application as Administrator."
            return f"⚠️ Error: {result.stderr.strip()}"
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "⚠️ Timeout: The response took too long. Try a simpler question."
    except PermissionError:
        return "⚠️ Permission Error: Run the app as Administrator or grant access to 'ollama'."
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

# Function for generating responses
def generate_answer(file_content, question):
    context = file_content[:1500]  # Reduced context length for better processing
    return ask_llama(question, context=context)

# Parallel execution for faster response
def async_generate_answer(file_content, question, result_container):
    result_container["answer"] = generate_answer(file_content, question)

# UI Header
st.title("📊 Log Analysis Portal")
st.markdown("Analyze logs efficiently with AI-powered summarization and insights.")

# File Upload
file = st.file_uploader("📂 Upload a log file (max size: 200MB)", type=["txt", "log", "pcap"])
file_content = None  # Ensure file_content is always defined

if file:
    try:
        raw_data = file.read()
        encoding_detected = chardet.detect(raw_data)['encoding'] or 'utf-8'
        file_content = raw_data.decode(encoding_detected, errors='replace')
        st.success("✅ File uploaded and processed successfully!")
    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")
        file_content = None

# Process user query
if file_content is not None:
    st.subheader("💬 Ask a question about the log content:")
    user_query = st.text_input("Type your question here and press Enter.")
    if user_query:
        with st.spinner("⏳ Processing your request..."):
            result_container = {}
            thread = threading.Thread(target=async_generate_answer, args=(file_content, user_query, result_container))
            thread.start()
            thread.join(timeout=90)  # Limit execution time
            answer = result_container.get("answer", "⚠️ Timeout: No response generated.")
            st.text_area("📌 Log Summarization Result:", value=answer, height=150)

# Footer
st.markdown("---")
st.markdown("🔗 **Stay Connected:** [GitHub](https://github.com/rajeshbakthavachalam/log-analysis-portal/) | [LinkedIn](https://www.linkedin.com/in/rajesh-b-a120a824/)")
