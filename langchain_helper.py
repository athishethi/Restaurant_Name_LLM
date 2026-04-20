from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

def generate_restaurant_name_and_items(cuisine):

    api_key = os.getenv("GROQ_API_KEY")

    # 🚨 Hard fail if key missing
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set. Add it in Streamlit secrets or .env")

    llm = ChatGroq(
        api_key=api_key,   # ✅ CORRECT PARAM
        model_name="llama3-8b-8192",
        temperature=0.7
    )

    prompt = PromptTemplate.from_template(
        "Suggest a fancy restaurant name for {cuisine} cuisine and list 5 menu items."
    )

    chain = prompt | llm

    response = chain.invoke({"cuisine": cuisine})

    return response.content
