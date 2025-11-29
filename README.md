# 🔮 AI Tarot Card Reader

Features:
- 78 Tarot cards (from tarot_cards.csv)
- AI-generated mystical images
- Download button for each card
- User login (streamlit_authenticator)
- Styled UI + button animation
- GitHub Actions CI/CD
- No pyarrow needed

---

## Deploy on Streamlit Cloud
1. Push repo to GitHub
2. Go to https://streamlit.io/cloud
3. Click "Deploy from GitHub"
4. Select main branch, entry point: app.py
5. Set OPENAI_API_KEY in secrets
6. Enjoy the app!

---

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
