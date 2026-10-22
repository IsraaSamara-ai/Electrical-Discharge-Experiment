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

APP_DIR = Path(__file__).resolve().parent


def find_html() -> Path | None:
    """يبحث عن ملف المختبر: يفضّل الاسم الأصلي، وإلا يأخذ أي ملف HTML في المستودع."""
    preferred = APP_DIR / "Lap_Atom_Structure_3d_ch-1.html"
    if preferred.exists():
        return preferred
    candidates = sorted(APP_DIR.rglob("*.html"))
    return candidates[0] if candidates else None


@st.cache_data
def load_lab(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


html_path = find_html()

if html_path is None:
    st.error(
        "لم يتم العثور على ملف المختبر (.html). "
        "تأكدي من رفعه إلى نفس مجلد app.py في مستودع GitHub."
    )
    st.write("الملفات الموجودة حالياً:", [p.name for p in APP_DIR.iterdir()])
else:
    components.html(load_lab(str(html_path)), height=1000, scrolling=True)
