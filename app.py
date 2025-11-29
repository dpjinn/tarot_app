import streamlit as st
from utils.tarot_loader import load_tarot_csv
from utils.tarot_generator import generate_tarot_image
from io import BytesIO
import random
import streamlit_authenticator as stauth

# -----------------------------
# Login
# -----------------------------
users = {"admin": "password123"}
authenticator = stauth.Authenticate(users, "tarot_cookie", "tarot_key", cookie_expiry_days=1)
name, authentication_status = authenticator.login("Login", "main")

if authentication_status:
    st.sidebar.success(f"Welcome {name}!")
elif authentication_status == False:
    st.sidebar.error("Username/password incorrect")
else:
    st.sidebar.warning("Please login")

# -----------------------------
# Main App
# -----------------------------
if authentication_status:
    st.set_page_config(page_title="🔮 AI Tarot", layout="wide", initial_sidebar_state="expanded")
    st.markdown(
        """
        <style>
        .stButton>button {background-color: #7F00FF; color:white; height:50px; width:200px; font-size:20px; border-radius:10px;}
        .stApp {background-image: url('https://images.unsplash.com/photo-1557682250-6a59140c6f0d'); background-size: cover;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🔮 AI Tarot Card Reader")
    tarot_cards = load_tarot_csv()

    if st.button("Draw 3 Cards"):
        selected_cards = random.sample(tarot_cards, 3)
        cols = st.columns(3)
        for idx, card in enumerate(selected_cards):
            with cols[idx]:
                st.subheader(card["name"])
                st.caption(card["meaning"])
                api_key = st.secrets["OPENAI_API_KEY"]
                img = generate_tarot_image(card["name"], api_key)
                st.image(img)
                
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                st.download_button("Download Card", buffer.getvalue(), f"{card['name']}.png")
