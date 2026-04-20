import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.set_page_config(page_title="Restaurant Generator")

st.title("🍽️ Restaurant Name Generator")

cuisine = st.text_input("Enter cuisine type")

if st.button("Generate"):
    if cuisine.strip():
        result = generate_restaurant_name_and_items(cuisine)
        st.success(result)
    else:
        st.warning("Please enter a cuisine type")
