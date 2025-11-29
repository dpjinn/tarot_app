import streamlit as st
from utils.tarot_loader import load_tarot_csv
from utils.tarot_generator import generate_tarot_image
from io import BytesIO
import random
import streamlit_authenticator as stauth

# -----------------------------
# User Authentication (Hashed Password)
# -----------------------------
# 비밀번호 해시화
hashed_passwords = stauth.Hasher(["password123"]).generate()

credentials = {
    "usernames": {
        "admin": {
            "name": "Admin User",
            "password": hashed_passwords[0]
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "tarot_cookie",    # cookie name
    "tarot_key",       # key name
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.sidebar.success(f"Welcome {name}!")
elif authentication_status is False:
    st.sidebar.error("Username/password incorrect")
else:
    st.sidebar.warning("Please login")

# -----------------------------
# Main App
# -----------------------------
if authentication_status:
    st.set_page_config(
        page_title="🔮 AI Tarot",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # UI 스타일
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #7F00FF; 
            color:white; 
            height:50px; 
            width:200px; 
            font-size:20px; 
            border-radius:10px;
        }
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1557682250-6a59140c6f0d'); 
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🔮 AI Tarot Card Reader")

    # CSV 로딩
    tarot_cards = load_tarot_csv("tarot_cards.csv")

    # Draw 3 Cards
    if st.button("Draw 3 Cards"):
        selected_cards = random.sample(tarot_cards, 3)
        cols = st.columns(3)

        api_key = st.secrets.get("OPENAI_API_KEY", None)
        if not api_key:
            st.error("Set your OPENAI_API_KEY in Streamlit secrets.toml")
        else:
            for idx, card in enumerate(selected_cards):
                with cols[idx]:
                    st.subheader(card["name"])
                    st.caption(card["meaning"])

                    # AI 이미지 생성
                    img = generate_tarot_image(card["name"], api_key)
                    st.image(img)

                    # 다운로드 버튼
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    st.download_button("Download Card", buffer.getvalue(), f"{card['name']}.png")
