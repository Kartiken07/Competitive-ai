# 🧠 Competitive AI Analysis Tool using Hugging Face & Streamlit

This project is a GenAI-powered competitive analysis tool built with **Python**, **Langchain**, and **Hugging Face Inference API**.  
It allows you to generate insights such as **SWOT Analysis**, **Funding Info**, **Tech Stack**, and **Business Model** for multiple companies using LLMs like **Mistral-7B**.

---

## 🚀 Features

- Accepts multiple company names and attributes as input
- Performs analysis using GenAI models via Hugging Face
- Generates CSV output of results
- Clean and customizable Python structure
- Ready for Streamlit deployment

---

## 🔐 Environment Setup

### 1. Clone the repository

bash
git clone https://github.com/Kartiken07/Competitive-ai
cd competitive_ai
python3 -m venv venv 


Create a Virtual Environment (Optional but Recommended) 


python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

Add Your Hugging Face API Key

HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here

streamlit run app.py


