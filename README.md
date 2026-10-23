# ReviewSense AI — NLP-Powered Customer Sentiment Analysis

An interactive Natural Language Processing (NLP) application that analyzes customer reviews, classifies sentiments, extracts keywords, and visualizes customer feedback using Python and Streamlit.

### 🚀 Live Demo

**[Try ReviewSense AI](https://reviewsense-noman.streamlit.app/)**

### ✨ Features

- **Sentiment Analysis:** Classifies customer reviews as Positive, Negative, or Neutral.
- **Single Review Analysis:** Analyze individual reviews instantly.
- **Bulk CSV Analysis:** Upload a dataset to analyze multiple customer reviews.
- **Keyword Extraction:** Identify frequently occurring words and phrases using CountVectorizer.
- **Interactive Dashboard:** Visualize sentiment distribution and review statistics.
- **Download Results:** Export analyzed reviews as CSV.

### 🧠 NLP Algorithm

This project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, a lexicon-based and rule-based sentiment analysis algorithm.

VADER analyzes text using sentiment-related vocabulary and linguistic rules for negation, capitalization, and emphasis. It generates a compound sentiment score between -1 and +1.

| Compound Score | Sentiment |
|---|---|
| ≥ 0.05 | Positive |
| ≤ -0.05 | Negative |
| Between -0.05 and 0.05 | Neutral |

The application also uses scikit-learn's **CountVectorizer** to identify common words and phrases across reviews.

### 🛠️ Tech Stack

- **Language:** Python
- **NLP:** VADER Sentiment
- **Text Features:** scikit-learn CountVectorizer
- **Data Processing:** pandas
- **Web Framework:** Streamlit
- **Data Visualization:** Plotly
- **Testing:** pytest
- **Deployment:** Streamlit Community Cloud

### ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/nomanpathan485/ReviewSense-AI.git
cd ReviewSense-AI
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### 📊 How It Works

1. User enters a review or uploads a CSV dataset.
2. Python processes the review text.
3. VADER calculates sentiment scores.
4. Each review receives a Positive, Negative, or Neutral label.
5. The application visualizes results and extracts keywords.
6. Users can download their analyzed reviews.

### 📁 Project Structure

```text
ReviewSense-AI/
├── app.py
├── nlp_engine.py
├── requirements.txt
├── sample_reviews.csv
├── test_nlp_engine.py
└── README.md
```

### 🎯 Applications

- E-commerce customer review analysis
- Customer satisfaction monitoring
- Product feedback analysis
- Service quality analysis
- Business review reporting

### 🔮 Future Improvements

- Transformer-based sentiment analysis using DistilBERT
- Multilingual support (Hindi and Marathi)
- Aspect-based sentiment analysis
- Automated review summarization
- More detailed feedback insights

### 👨‍💻 Developed By

**Noman Pathan**  
AI & Data Science Engineering Student

**GitHub:** https://github.com/nomanpathan485

**Live Application:** https://reviewsense-noman.streamlit.app/

---

*Built with Python, NLP, and Streamlit.*