# app.py
import streamlit as st
from state.session_manager import initialize_state, get_fact, set_fact
from ui.components import display_greeting, display_fact_box, display_buttons
from core.facts_service import get_random_fact

# ---- Initialize session state ----
initialize_state()

# ---- Load a fact on first visit ----
if not get_fact():
    fact = get_random_fact()
    set_fact(fact)

# ---- UI Layout ----
st.set_page_config(
    page_title="Fun Fact Generator",
    page_icon="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-lnKzg2lI0G2QAViUgRCY70jGRsQ6qc.png&w=320&q=75",
    layout="centered",
    initial_sidebar_state="collapsed"
)

display_greeting()
display_fact_box()
display_buttons()
