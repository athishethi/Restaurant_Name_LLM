import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.title("Restaurant Name Generator 🍽️")

cuisine = st.text_input("Enter cuisine type")

if cuisine:
    result = generate_restaurant_name_and_items(cuisine)
    st.write(result)
