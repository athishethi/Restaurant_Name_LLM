import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


# ✅ Initialize LLM properly using environment variable
llm = ChatGroq(
    model_name="llama3-8b-8192",   # safer default model
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
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
    name_response = name_chain.invoke({"cuisine": cuisine})
    name = name_response.content.strip().replace('"', '')

    # Step 2 → Generate menu
    menu_response = food_items_chain.invoke({
        "restaurant_name": name
    })
    menu = menu_response.content.strip()

    return {
        "restaurant_name": name,
        "menu_items": menu.split(", ")
    }


# For testing
if __name__ == "__main__":
    response = generate_restaurant_name_and_items("Indian")
    print(response)
