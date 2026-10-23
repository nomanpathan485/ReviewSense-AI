"""Core natural language processing utilities for ReviewSense AI."""
from __future__ import annotations

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()


def analyze_review(text: str) -> dict:
    """Analyze one English-language review using VADER's compound score."""
    text = str(text).strip()
    if not text:
        return {"sentiment": "Neutral", "score": 0.0}
    score = _analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        label = "Positive"
    elif score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return {"sentiment": label, "score": round(score, 4)}


def analyze_dataframe(frame: pd.DataFrame, text_column: str) -> pd.DataFrame:
    """Return an annotated copy, without mutating the uploaded data."""
    output = frame.copy()
    output[text_column] = output[text_column].fillna("").astype(str)
    results = output[text_column].map(analyze_review)
    output["sentiment"] = results.map(lambda row: row["sentiment"])
    output["score"] = results.map(lambda row: row["score"])
    return output


def extract_keywords(texts, max_features: int = 12, ngram_range=(1, 2)) -> pd.DataFrame:
    """Count meaningful unigrams and bigrams (not topic modeling)."""
    clean = [str(text).strip() for text in texts if str(text).strip()]
    if not clean:
        return pd.DataFrame(columns=["keyword", "frequency"])
    vectorizer = CountVectorizer(
        stop_words="english", ngram_range=ngram_range,
        max_features=max_features, token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z]+\b",
    )
    try:
        matrix = vectorizer.fit_transform(clean)
    except ValueError:  # e.g., input contains stop words only
        return pd.DataFrame(columns=["keyword", "frequency"])
    counts = matrix.sum(axis=0).A1
    return (pd.DataFrame({"keyword": vectorizer.get_feature_names_out(), "frequency": counts})
            .sort_values(["frequency", "keyword"], ascending=[False, True])
            .reset_index(drop=True))
