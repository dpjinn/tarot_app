import streamlit as st
import pandas as pd
import os
from utils.data_utils import (
    save_csv, load_csv,
    save_json, load_json,
    save_parquet_no_pyarrow, load_parquet_no_pyarrow
)

st.set_page_config(page_title="GitHub + Streamlit Data Utility", layout="wide")

st.title("📂 Data Utility App (GitHub + Streamlit Cloud)")
st.write("Upload → Preview → Save → Re-Download | No pyarrow needed.")

menu = st.sidebar.selectbox("Menu", ["Upload & Preview", "Save Formats", "Load Parquet"])

uploaded_df = None

# -------------------------
# 1) Upload & Preview
# -------------------------
if menu == "Upload & Preview":
    st.subheader("Upload CSV or JSON")
    uploaded = st.file_uploader("Upload File", type=["csv", "json"])

    if uploaded:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_json(uploaded)

        st.success("File loaded!")
        st.dataframe(df)

        st.session_state["df"] = df

# -------------------------
# 2) Save Formats
# -------------------------
elif menu == "Save Formats":
    st.subheader("Save Uploaded DataFrame")
    
    if "df" not in st.session_state:
        st.warning("Upload a file first!")
    else:
        df = st.session_state["df"]
        file_type = st.selectbox("Choose Format", ["CSV", "JSON", "Parquet (DuckDB)"])
        filename = st.text_input("File Name (ex: output.csv)")

        if st.button("Save File"):
            if filename == "":
                st.error("Enter a valid file name")
            else:
                path = filename

                if file_type == "CSV":
                    save_csv(df, path)
                elif file_type == "JSON":
                    save_json(df, path)
                elif file_type == "Parquet (DuckDB)":
                    save_parquet_no_pyarrow(df, path)

                with open(path, "rb") as f:
                    st.download_button("Download File", f, path)

# -------------------------
# 3) Load Parquet (DuckDB)
# -------------------------
elif menu == "Load Parquet":
    st.subheader("Load a Parquet File (No pyarrow needed)")

    uploaded = st.file_uploader("Upload Parquet", type=["parquet"])

    if uploaded:
        temp_path = "temp.parquet"
        with open(temp_path, "wb") as f:
            f.write(uploaded.read())

        df = load_parquet_no_pyarrow(temp_path)
        st.dataframe(df)
        st.session_state["df"] = df
