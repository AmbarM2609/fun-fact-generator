# state/session_manager.py
import streamlit as st

FACT_KEY = "current_fact"        # key to store current fact in session state
PREV_FACT_KEY = "previous_fact"  # key to store last fact (avoid repeats)

def initialize_state():
    """
    Initializes session state keys if not already present.
    Call this at the start of the app.
    """
    if FACT_KEY not in st.session_state:
        st.session_state[FACT_KEY] = None
    if PREV_FACT_KEY not in st.session_state:
        st.session_state[PREV_FACT_KEY] = None

def set_fact(new_fact: str):
    """
    Updates session state with a new fact.
    """
    st.session_state[PREV_FACT_KEY] = st.session_state.get(FACT_KEY)
    st.session_state[FACT_KEY] = new_fact

def get_fact() -> str:
    """
    Returns the current fact from session state.
    """
    return st.session_state.get(FACT_KEY, "No fact loaded yet.")
