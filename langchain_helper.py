from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os

def generate_restaurant_name_and_items(cuisine):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192",
        temperature=0.7
    )

    prompt_template = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest a fancy restaurant name for {cuisine} cuisine and list 5 menu items."
    )

    prompt = prompt_template.format(cuisine=cuisine)

    response = llm.invoke(prompt)

    return response.content
