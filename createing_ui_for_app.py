import streamlit as st
from main import main 
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Competitive AI Analysis", page_icon="🧠", layout="centered")
st.header("🤖 Competitive AI Analysis App")
company_name=st.text_input("Enter Your Company Name(Comma Seperated)",placeholder="e.g. OpenAI, Anthropic, Cohere")
atts=st.text_input("Enter The options(Comma Seperated)",placeholder="e.g. accuracy, speed, latency")
analysis_type = st.selectbox(
    "Choose a analysis_type",
    ["SWOT Analysis", "Funding & Valuation", "TechStack", "Bussiness"]
)
if st.button("Run Analysis"):
    result = main(company_name, atts,analysis_type)
    with open(result, "rb") as f:
        st.download_button("Download CSV", f, file_name="analysis.csv")