from transformers import pipeline
import pandas as pd

def analyze_texts(texts):
    sentiment_analyzer = pipeline("sentiment-analysis")
    results = []
    for text in texts:
        sentiment = sentiment_analyzer(text[:512])[0]
        results.append({
            "text": text,
            "label": sentiment['label'],
            "score": sentiment['score']
        })
    return pd.DataFrame(results)
