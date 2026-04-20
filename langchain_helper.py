from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.environ.get("GROQ_API_KEY", "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")
)

# Prompt 1 → Restaurant name
prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="""
Suggest ONE fancy restaurant name for {cuisine} cuisine.
Return ONLY the restaurant name.
Do not give explanation.
"""
)

name_chain = prompt_template_name | llm

# Prompt 2 → Menu items
prompt_template_items = PromptTemplate(
    input_variables=["restaurant_name"],
    template="""
Suggest 8 menu items for the restaurant {restaurant_name}.
Return ONLY comma separated menu items.
Do not include explanation.
"""
)

food_items_chain = prompt_template_items | llm


def generate_restaurant_name_and_items(cuisine):
    # Step 1 → Generate restaurant name
    name = name_chain.invoke({"cuisine": cuisine}).content

    # Step 2 → Generate menu items
    menu = food_items_chain.invoke({
        "restaurant_name": name
    }).content

    return {
        "restaurant_name": name,
        "menu_items": menu
    }

if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Indian")
    print(response)
