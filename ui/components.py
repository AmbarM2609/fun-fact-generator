
# ui/components.py
import streamlit as st
from state.session_manager import get_fact, set_fact
from core.facts_service import get_random_fact

def display_greeting():
    st.title("Fun Facts", text_alignment="center")
    st.divider()
    st.markdown("""
                ##### Instructions :
                * Click the "New Fact" button below to generate a new fun fact 
                * Click the "Copy Fact" button to copy the current fact to the clipboard.""")
    st.divider()

def display_fact_box():
    fact = get_fact()
    st.markdown("""#### Did You Know..?""", )
    st.info(fact, icon="👉")  # highlights the fact
    st.divider()

def generate_new_fact():
    new_fact = get_random_fact()
    # Avoid immediate repeat
    while new_fact == get_fact():
        new_fact = get_random_fact()
    set_fact(new_fact)

def display_buttons():
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("New Fact"):
            generate_new_fact()
    with col2:
        fact = get_fact()
        if fact:
            st.button(
                "Copy Fact",
                on_click=copy_to_clipboard,
                args=(fact,)
            )

def copy_to_clipboard(text: str):
    # Uses Streamlit's built-in clipboard support
    st.code(text, language="text")
    #st.query_params()  # placeholder for clipboard action
    st.success("COPY FROM ABOVE!")
