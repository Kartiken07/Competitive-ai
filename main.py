from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import csv

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "ADD_YOUR_HUGGING_FACE_TOKEN"
def api_call_data(company_name, attributes, analysis_type):
    company_data = {}

    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="text-generation",
        uggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
    )

    model = ChatHuggingFace(llm=llm)

    company_name = get_data_name(company_name)
    attributee = get_data_atibutes(attributes)

    if analysis_type == "SWOT Analysis":
        prompt = "Perform a detailed SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis for the company. Output only final answer. No reasoning, no steps, no analysis. Exactly 10–15 words only and don't add 'user wants this' type of words."
    elif analysis_type == "Funding & Valuation":
        prompt = "Provide a comprehensive overview of the funding and valuation history of company. Output only final answer. No reasoning, no steps, no analysis. Exactly 10–15 words only and don't add 'user wants this' type of words."
    elif analysis_type == "TechStack":
        prompt = "Analyze the technology stack used by company to build and deliver its AI solutions. Output only final answer. No reasoning, no steps, no analysis. Exactly 10–15 words only and don't add 'user wants this' type of words."
    elif analysis_type == "Bussiness":
        prompt = "Describe the business model of company in detail. Output only final answer. No reasoning, no steps, no analysis. Exactly 10–15 words only and don't add 'user wants this' type of words."

    for company in company_name:
        ruf = []
        for attribute in attributee:
            try:
                response = model.invoke(f"{company}'s {attribute}. {prompt}")
                result = response.content.strip().replace("<think>", "").replace("</think>", "").replace("\n", " ").replace("/n", " ")
            except Exception as e:
                result = f"Error: {e}"

            ruf.append(result)
        company_data[company] = ruf

    return company_data, attributee

def get_data_name(company_name):
    return [c.strip() for c in company_name.split(",")]

def get_data_atibutes(attributes):
    return [a.strip() for a in attributes.split(",")]

def convert_to_csv(data, attributes, filename="output.csv"):
    headers = ["Company"] + list(attributes)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for company, values in data.items():
            writer.writerow([company] + values)
    return filename

def main(company_name, attributes, analysis_type):
    yo, attribute = api_call_data(company_name, attributes, analysis_type)
    x = convert_to_csv(yo, attribute)
    return x

if __name__ == "__main__":
    main("OpenAI,Anthropic", "accuracy,speed", "SWOT Analysis")
