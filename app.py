import streamlit as st
import traceback
from langchain_helper import generate_restaurant_name_and_items

# Page config
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️")

st.title("Restaurant Name Generator 🍽️")

# Input
cuisine = st.text_input("Enter cuisine type")

# Button instead of auto-trigger (prevents unnecessary API calls)
if st.button("Generate"):
    if not cuisine.strip():
        st.warning("Please enter a cuisine type")
    else:
        try:
            with st.spinner("Generating restaurant name..."):
                result = generate_restaurant_name_and_items(cuisine)

            # Handle different response types
            if isinstance(result, dict):
                st.subheader("Restaurant Name")
                st.write(result.get("restaurant_name", "N/A"))

                st.subheader("Menu Items")
                items = result.get("menu_items", [])
                for item in items:
                    st.write(f"- {item}")

            else:
                # fallback (if function returns plain text)
                st.write(result)

        except Exception as e:
            st.error("Something went wrong")
            st.text(traceback.format_exc())
