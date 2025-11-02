import streamlit as st
import pandas as pd
from utils.text_analysis import analyze_texts

st.set_page_config(page_title="Marine Ecosystem Insights", layout="wide")

st.title("🌊 AI-Powered Insights for Marine Ecosystem Health")
st.write("Analyze text data related to oceans, marine life, and environmental reports using NLP.")

uploaded_file = st.file_uploader("Upload a text file containing marine-related content", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    texts = text.split("\n")
    df = analyze_texts(texts)
    st.subheader("Sentiment Analysis Results")
    st.dataframe(df)

    st.bar_chart(df["label"].value_counts())
else:
    st.info("Upload a `.txt` file to begin analysis.")
