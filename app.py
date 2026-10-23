"""Streamlit UI for customer review sentiment analysis."""
from pathlib import Path
import pandas as pd
import streamlit as st
from nlp_engine import analyze_review, analyze_dataframe, extract_keywords

st.set_page_config(page_title="ReviewSense AI", page_icon="💬", layout="wide")
st.markdown("""<style>
.block-container {padding-top: 2rem; max-width: 1100px;}
h1 {letter-spacing:-.04em;}
[data-testid="stMetric"] {background:rgba(110,110,150,.09);padding:16px;border-radius:14px;}
</style>""", unsafe_allow_html=True)
st.title("💬 ReviewSense AI")
st.caption("Understand what your customers are saying · English review sentiment & keyword insights")

single, batch = st.tabs(["🔎 Analyze one review", "📊 Analyze a CSV dataset"])
with single:
    st.subheader("Instant sentiment analysis")
    review = st.text_area("Type an English customer review", value="The product quality is amazing, but delivery was slow.", height=130)
    if st.button("Analyze sentiment", type="primary"):
        if not review.strip():
            st.warning("Please enter a review first.")
        else:
            result = analyze_review(review)
            symbol = {"Positive": "🟢", "Neutral": "⚪", "Negative": "🔴"}[result["sentiment"]]
            st.success(f"{symbol} Predicted sentiment: {result['sentiment']}")
            st.metric("VADER compound score", f"{result['score']:+.4f}")
            st.caption("Scores range from -1 to +1. This score is not a probability or accuracy measure.")

with batch:
    st.subheader("Customer feedback dashboard")
    st.write("Upload a CSV containing a column of English-language review text, or use our example dataset.")
    uploaded = st.file_uploader("Choose a CSV file", type=["csv"])
    use_example = st.checkbox("Use included example dataset", value=True if uploaded is None else False)
    try:
        if uploaded is not None:
            data = pd.read_csv(uploaded)
        elif use_example:
            data = pd.read_csv(Path(__file__).parent / "data" / "sample_reviews.csv")
        else:
            data = None
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError, pd.errors.EmptyDataError) as exc:
        st.error(f"Unable to read CSV: {exc}")
        data = None

    if data is not None:
        if data.empty or len(data.columns) == 0:
            st.warning("This CSV has no rows or columns to analyze.")
        else:
            column = st.selectbox("Select the column containing reviews", list(data.columns), index=list(data.columns).index("review") if "review" in data.columns else 0)
            if len(data) > 5000:
                st.warning("For responsiveness, the first 5,000 reviews are analyzed.")
                data = data.head(5000)
            analyzed = analyze_dataframe(data, column)
            counts = analyzed["sentiment"].value_counts().reindex(["Positive", "Neutral", "Negative"], fill_value=0)
            a, b, c, d = st.columns(4)
            a.metric("Total reviews", f"{len(analyzed):,}")
            b.metric("Positive", int(counts["Positive"]))
            c.metric("Neutral", int(counts["Neutral"]))
            d.metric("Negative", int(counts["Negative"]))
            st.subheader("Sentiment distribution")
            st.bar_chart(counts.rename("Number of reviews"))
            st.subheader("Frequent words and phrases")
            keywords = extract_keywords(analyzed[column])
            if keywords.empty:
                st.info("No meaningful keywords found in these reviews.")
            else:
                st.bar_chart(keywords.set_index("keyword")["frequency"])
            st.subheader("Analyzed reviews")
            choice = st.selectbox("Filter sentiment", ["All", "Positive", "Neutral", "Negative"])
            visible = analyzed if choice == "All" else analyzed[analyzed["sentiment"] == choice]
            st.dataframe(visible, use_container_width=True, hide_index=True)
            st.download_button("⬇️ Download analyzed CSV", data=analyzed.to_csv(index=False).encode("utf-8"), file_name="reviewsense_results.csv", mime="text/csv")
            st.caption("Disclaimer: Sentiment is estimated by a rule-based model; mixed sentiment, sarcasm and non-English text may be misclassified. Uploaded files are processed in app memory.")
