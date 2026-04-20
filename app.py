import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.set_page_config(page_title="Restaurant Generator")

st.title("🍽️ Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a cuisine",
    ("Indian", "Italian", "Mexican", "Arabic")
)

if st.sidebar.button("Generate"):
    response = generate_restaurant_name_and_items(cuisine)

    # Restaurant Name
    st.header(response['restaurant_name'])

    # Menu Items (already a list ✅)
    st.subheader("Menu Items")
    for item in response['menu_items']:
        st.write(f"- {item.strip()}")
