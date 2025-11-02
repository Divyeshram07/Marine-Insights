import streamlit as st
from textblob import TextBlob

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="🌊 Marine Insights", page_icon="🌊")

# -------------------- TITLE & DESCRIPTION --------------------
st.title("🌊 AI-Powered Insights for Marine Ecosystem Health")
st.write("Analyze marine-related text for sentiment and extract environmental keywords.")

# -------------------- USER INPUT --------------------
text_input = st.text_area(
    "Enter marine-related text:",
    "Coral reefs are dying due to rising sea temperatures and pollution."
)

# -------------------- ANALYSIS --------------------
if st.button("Analyze"):
    st.info("Analyzing text...")

    blob = TextBlob(text_input)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

    # Sentiment Results
    st.subheader("🔍 Sentiment Analysis")
    st.write(f"**Label:** {sentiment}")
    st.write(f"**Polarity Score:** {polarity:.2f}")

    # Marine Keywords Extraction
    st.subheader("🌐 Key Environmental Terms")
    marine_terms = [
        "coral", "pollution", "ocean", "plastic", "fish", "reef",
        "acidification", "warming", "marine", "biodiversity"
    ]
    keywords = [word for word in text_input.lower().split() if word in marine_terms]

    if keywords:
        st.success(", ".join(set(keywords)))
    else:
        st.warning("No specific marine-related keywords found.")
