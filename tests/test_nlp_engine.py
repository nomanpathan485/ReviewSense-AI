import pandas as pd
from nlp_engine import analyze_review, analyze_dataframe, extract_keywords


def test_sentiments():
    assert analyze_review("Absolutely wonderful, I love this!")["sentiment"] == "Positive"
    assert analyze_review("Terrible, awful and disappointing!")["sentiment"] == "Negative"
    assert analyze_review("")["sentiment"] == "Neutral"


def test_dataframe_does_not_mutate_input():
    original = pd.DataFrame({"review": ["Excellent", None]})
    result = analyze_dataframe(original, "review")
    assert len(result) == 2
    assert "sentiment" in result
    assert pd.isna(original.loc[1, "review"])


def test_keywords():
    words = extract_keywords(["fast delivery", "fast shipping"])
    assert "fast" in words["keyword"].values
    assert extract_keywords(["the", "and"]).empty
