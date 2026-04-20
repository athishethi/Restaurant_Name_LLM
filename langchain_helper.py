from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os

def generate_restaurant_name_and_items(cuisine):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found. Check your .env file.")

    llm = ChatGroq(
        api_key=api_key,
        model_name="llama3-8b-8192",
        temperature=0.7
    )

    prompt = PromptTemplate.from_template(
        "Suggest a fancy restaurant name for {cuisine} cuisine and list 5 menu items."
    )

    chain = prompt | llm

    response = chain.invoke({"cuisine": cuisine})

    return response.content
