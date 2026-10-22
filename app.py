from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="مختبر الكيمياء الافتراضي - بنية الذرة",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# إخفاء عناصر ستريملت الزائدة وتوسيع المساحة للمختبر
st.markdown(
    """
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_FILE = Path(__file__).parent / "Lap_Atom_Structure_3d_ch-1.html"


@st.cache_data
def load_lab() -> str:
    return HTML_FILE.read_text(encoding="utf-8")


components.html(load_lab(), height=1000, scrolling=True)
