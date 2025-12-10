# ui/components.py
import streamlit as st
from state.session_manager import get_fact, set_fact
from core.facts_service import get_random_fact

# -------------------------------------------------------
# Inject Neobrutalist CSS (dark matte blue background)
# -------------------------------------------------------
def inject_styles():
    st.markdown(
         """
        <style>
        /* -----------------------------------------
           COLOR VARIABLES (Your Palette)
        ----------------------------------------- */
        :root {
            --color-background: #F7F4EC;
            --color-text: #2C1E14;
            --color-primary-tag: #3CB05C;
            --color-secondary-tag: #E96C5F;
            --color-button-main: #EC6469;
        }

        /* -----------------------------------------
           GLOBAL BACKGROUND + FONT
        ----------------------------------------- */
        html, body, [data-testid="stAppViewContainer"] {
            background: var(--color-background) !important;
            color: var(--color-text) !important;
            font-family: "Inter", sans-serif;
        }

        /* -----------------------------------------
           TITLE (Neobrutalist Block)
        ----------------------------------------- */
        .nb-title {
            text-align: center;
            font-weight: 800;
            font-size: 2.4rem;
            padding: 16px 24px;
            margin: 20px auto;
            background: #ffffff;
            color: var(--color-text);
            border: 6px solid var(--color-text);
            border-left-width: 10px;
            border-left-color: var(--color-button-main);  /* tie-in highlight */
            border-radius: 12px;
            max-width: 650px;
            box-shadow: 10px 10px 0px rgba(0,0,0,0.20);
        }

        /* -----------------------------------------
           INSTRUCTION CARD
        ----------------------------------------- */
        .nb-card {
            background: #ffffff;
            padding: 18px;
            margin: 14px 0 22px;
            border: 4px solid var(--color-text);
            border-right-width: 10px;
            border-right-color: var(--color-secondary-tag);
            border-radius: 10px;
            box-shadow: 10px 10px 0px rgba(0,0,0,0.2);
            color: var(--color-text);
        }

        .nb-card ul {
            padding-left: 20px;
        }

        /* -----------------------------------------
           FACT HEADER
        ----------------------------------------- */
        .nb-fact-header {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--color-text);
            background: var(--color-secondary-tag);
            padding: 12px 18px;
            border-radius: 10px;
            display: block;
            margin-left: auto;
            margin-right: auto; 
            width: fit-content;
            box-shadow: 4px 4px 0px #2C1E14;
            margin-bottom: 10px;
        }

        /* FACT CARD */
        .nb-fact-card {
            background: var(--color-background);
            border: 3px solid var(--color-text);
            border-radius: 8px;
            padding: 20px;
            font-size: 1.4rem;
            color: var(--color-text);
            font-weight: 800;

            box-shadow: 6px 6px 0px #2C1E14;
            margin-top: 10px;
            margin-bottom: 20px;
        }

        /* FACT ICON */
        .nb-fact-icon {
            font-size: 1.4rem;
            margin-right: 8px;
        }

        /* -----------------------------------------
           ALERT BOX (Fact Display)
        ----------------------------------------- */
        .stAlert {
            border: 4px solid var(--color-text) !important;
            border-radius: 10px !important;
            box-shadow: 6px 6px 0px rgba(0,0,0,0.20) !important;
        }

        /* -----------------------------------------
           BUTTONS — Neobrutalist with Palette
        ----------------------------------------- */
        .stButton>button {
            background: #ffffff !important;
            text-align: center;
            color: var(--color-text) !important;
            border: 4px solid var(--color-text) !important;
            border-right-width: 10px !important;
            border-right-color: var(--color-button-main) !important;
            font-weight: 800 !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            box-shadow: 6px 6px 0px rgba(0,0,0,0.20) !important;
        }

        .stButton>button:hover {
            background: var(--color-button-main) !important;
            color: white !important;
            border-right-color: #b93d43 !important;
        }
        
        /* CUSTOM BUTTON: New Fact */
        .btn-new-fact > button {
            border-right-color: var(--color-secondary-tag) !important;
            background: #fffbe6 !important;
        }

        /* CUSTOM BUTTON: Copy Fact */
        .btn-copy-fact > button {
            border-right-color: var(--color-primary-tag) !important;
            background: #e6fff5 !important;
            text-align: left !important;   
        }

        /* -----------------------------------------
           GREEN + RED TAGS (Optional Feature)
        ----------------------------------------- */

        .tag-primary {
            background: var(--color-primary-tag);
            color: white;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 700;
            display: inline-block;
        }

        .tag-secondary {
            background: var(--color-secondary-tag);
            color: white;
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 700;
            display: inline-block;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------------
# UI Components
# -------------------------------------------------------

def display_greeting():
    inject_styles()  # apply CSS once

    st.markdown('<div class="nb-title">Fun Facts</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="nb-card">
            <h3 style="margin:0; font-weight:500;font-size: 1.4rem;">Instructions:</h3>
            <ul>
                <li>Click <b>“New Fact”</b> to generate a new fun fact.</li>
                <li >Click <b>“Copy Fact”</b> to copy the current fact.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


def display_fact_box():
    fact = get_fact()

    # Neo-Brutalist Header
    st.markdown('<div class="nb-fact-header">Did You Know…?</div>', unsafe_allow_html=True)

    # Neo-Brutalist Fact Card
    fact_html = f"""
        <div class="nb-fact-card">
            <span class="nb-fact-icon">👉</span> {fact}
        </div>
    """
    st.markdown(fact_html, unsafe_allow_html=True)


def generate_new_fact():
    new_fact = get_random_fact()
    while new_fact == get_fact():
        new_fact = get_random_fact()
    set_fact(new_fact)


def display_buttons():
    col1, col2 = st.columns([4, 1])

    # --- New Fact button ---
    with col1:
        st.markdown('<div class="btn-new-fact">', unsafe_allow_html=True)
        if st.button("New Fact", key="btn_new_fact"):
            generate_new_fact()
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Copy Fact button ---
    with col2:
        fact = get_fact()
        st.markdown('<div class="btn-copy-fact">', unsafe_allow_html=True)
        if fact:
            st.button(
                "Copy Fact",
                key="btn_copy_fact",
                on_click=copy_to_clipboard,
                args=(fact,),
            )
        st.markdown("</div>", unsafe_allow_html=True)



def copy_to_clipboard(text: str):
    st.code(text, language="text")
    st.success("Copy the text from above!")
