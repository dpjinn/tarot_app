import streamlit as st
from openai import OpenAI
from tarot_reader import draw_three_cards, make_prompt
from PIL import Image
import base64
import io

# --- OpenAI Client ---
client = OpenAI()

st.set_page_config(page_title="Tarot Reader", layout="wide")
st.title("🔮 AI Tarot Card Reader")
st.write("This app generates Tarot card images using the OpenAI Image API (DALL·E 3).")

if "cards" not in st.session_state:
    st.session_state.cards = None
if "images" not in st.session_state:
    st.session_state.images = None

if st.button("Draw 3 Tarot Cards"):
    st.session_state.cards = draw_three_cards()
    st.session_state.images = []

    for card in st.session_state.cards:
        prompt = make_prompt(card)
        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="512x512"
        )

        img_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(img_base64)
        image = Image.open(io.BytesIO(image_bytes))

        st.session_state.images.append(image)

if st.session_state.cards:
    st.subheader("Your Tarot Cards")

    cols = st.columns(3)
    for i, card in enumerate(st.session_state.cards):
        with cols[i]:
            st.image(st.session_state.images[i], caption=card)
