from langchain_groq import ChatGroq

def generate_restaurant_name_and_items(cuisine):
    llm = ChatGroq(
        temperature=0.7,
        groq_api_key="your_groq_api_key",
        model_name="llama3-70b-8192"
    )

    prompt = f"Suggest a fancy restaurant name for {cuisine} food. Also suggest 5 menu items."

    response = llm.invoke(prompt)

    return response.content
