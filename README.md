# tarot_app

# Streamlit Data Utility App (No PyArrow)

This repository provides a Streamlit application that:
- Uploads CSV/JSON
- Previews data
- Saves as CSV / JSON / Parquet
- Loads Parquet without pyarrow
- Fully compatible with Streamlit Cloud deployment
- Uses DuckDB instead of pyarrow

---

## 🚀 Deploy on Streamlit Cloud

1. Push this repository to GitHub  
2. Go to: https://streamlit.io/cloud  
3. Click **“Deploy from GitHub”**  
4. Select this repository  
5. Choose:
   - Entry point → `app.py`

You're ready!

---

## 💻 Run Locally (Windows/Mac)

### Install
```bash
pip install -r requirements.txt
