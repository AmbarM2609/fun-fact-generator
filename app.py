# app.py
import streamlit as st
import streamlit.components.v1 as components # for html meta tags injection
from state.session_manager import initialize_state, get_fact, set_fact
from ui.components import display_greeting, display_fact_box, display_buttons
from core.facts_service import get_random_fact

# **YOU MUST REPLACE THESE PLACEHOLDERS WITH YOUR ACTUAL DATA**
APP_URL = "https://[fun-fact-generator-by-ambar-mestry].streamlit.app"  # Your app's public URL
PREVIEW_TITLE = "Fun Fact Generator"
PREVIEW_DESCRIPTION = "A simple, clean, and interactive app built with Streamlit to deliver random, interesting facts."
PREVIEW_IMAGE_URL = "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-lnKzg2lI0G2QAViUgRCY70jGRsQ6qc.png&w=320&q=75" # Your social preview image

# --- METADATA INJECTION FUNCTION ---
def inject_meta_tags():
    """Injects Open Graph meta tags into the Streamlit app's HTML header."""
    meta_tags = f"""
        <head>
            <meta property="og:title" content="{PREVIEW_TITLE}" />
            <meta property="og:description" content="{PREVIEW_DESCRIPTION}" />
            <meta property="og:image" content="{PREVIEW_IMAGE_URL}" />
            <meta property="og:url" content="{APP_URL}" />
            <meta property="og:type" content="website" />
        </head>
    """
    # Use components.html to inject the tags. Set height/width to 0 to make it invisible.
    components.html(meta_tags, height=0, width=0)

# -------------------------------------------------------------

# ---- Initialize session state ----
initialize_state()

# ---- Load a fact on first visit ----
if not get_fact():
    fact = get_random_fact()
    set_fact(fact)

# ---- UI Configuration and Layout ----

# 1. Inject the OG tags right after initialization
inject_meta_tags() 

# 2. Set page config (already correct in your original code)
st.set_page_config(
    page_title=PREVIEW_TITLE, # Using the preview title here for consistency
    page_icon=PREVIEW_IMAGE_URL,
    layout="centered",
    initial_sidebar_state="collapsed"
)

display_greeting()
display_fact_box()
display_buttons()
