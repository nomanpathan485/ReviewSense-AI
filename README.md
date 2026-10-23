# 💬 ReviewSense AI — Customer Feedback NLP Dashboard

An end-to-end, English-language NLP project that performs rule-based sentiment analysis on individual customer reviews and uploaded CSV files, displays aggregate charts, extracts frequent words/phrases, and exports results. Built with Python, VADER, scikit-learn, pandas and Streamlit. No paid API key is needed.

## Features
- Analyze one review or upload a CSV of reviews
- Classify each review as Positive, Neutral or Negative
- Display VADER compound score (-1 to +1)
- Sentiment counts and interactive bar chart
- Frequent words and two-word phrases (CountVectorizer)
- Filter results and download analyzed CSV
- Included sample dataset and automated tests

## Installation (VS Code / Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
Open the local URL printed in the terminal, typically http://localhost:8501.
On macOS/Linux use `source .venv/bin/activate` instead of the PowerShell activation command.

## How it works
1. `app.py` collects review text or CSV input using Streamlit.
2. `nlp_engine.py` calls the VADER `SentimentIntensityAnalyzer` for each review.
3. VADER computes a normalized *compound* sentiment score (-1 to +1); we label scores >=0.05 Positive, <=-0.05 Negative, otherwise Neutral.
4. In batch mode, pandas adds `sentiment` and `score` columns to a copy of the uploaded DataFrame.
5. scikit-learn `CountVectorizer` tokenizes text, removes common English stop words and counts unigrams/bigrams to identify frequent phrases. This is frequency extraction, not true topic modeling.
6. Streamlit displays distributions and lets users download an annotated CSV.

## Project structure
```
reviewsense-ai/
├── app.py                   # Streamlit interface
├── nlp_engine.py            # Reusable NLP functions
├── data/sample_reviews.csv  # Demo data
├── tests/test_nlp_engine.py # Automated sanity tests
├── .streamlit/config.toml   # UI theme
├── requirements.txt         # Python dependencies
└── README.md
```

## Deploy for free
1. Create a GitHub repository (for example, `reviewsense-ai`) and upload the full project with `app.py` and `requirements.txt` in the repository root.
2. Visit https://share.streamlit.io/ and sign in using GitHub.
3. Create an app; select your repository, `main` branch and `app.py` as the entrypoint.
4. Deploy. Streamlit installs the requirements and provides a shareable `streamlit.app` URL.

## Tests
Install pytest (`python -m pip install pytest`) and run `python -m pytest -q`.

## Limitations and next improvements
VADER is lexicon/rule based, not a trained transformer. It is aimed at English and may struggle with domain jargon, irony, sarcasm, long mixed-sentiment reviews, and multilingual text. Compound scores are **not** confidence probabilities. Counts of terms are **not** semantic topic clusters. As a next stage, evaluate on labeled reviews and compare a fine-tuned transformer model; add aspect-based sentiment analysis to tell what users think about *price*, *delivery* and *quality* individually.

## Interview explanation
"I built a Streamlit customer-feedback NLP dashboard. I separated the UI from the NLP engine, used VADER to score sentiment and CountVectorizer to find frequent phrases, added batch CSV analysis and export, and designed it to deploy on Streamlit Community Cloud with no API keys. I understand the limitations of rule-based sentiment and would benchmark a transformer next."
