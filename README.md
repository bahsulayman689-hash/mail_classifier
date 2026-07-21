# mail_classifier
# 📧 Spam & Phishing Email Detector

A real-time, interactive Machine Learning web application that anatomizes text structure to classify SMS and email messages as **Spam** or **Ham (Legitimate)**. Built with Python, Scikit-Learn, and Streamlit.

🚀 **Live Demo:** [https://mailclassifier-rumaemmcsqmahmtv3q29jp.streamlit.app/]

---

## 🧠 How It Works & Detection Layers

Unlike basic filters, this system uses an optimized **Logistic Regression** model paired with a custom structural tokenizer to analyze text patterns step-by-step across three security layers:

1. **Case-Sensitive Signal Check (`lowercase=False`)**  
   Maps exact casing profiles. Standard words are processed normally, while high-stress, all-caps terms (`URGENT`, `FREE`, `LOCKED`) are flagged as high-risk spam indicators.
2. **Contextual Mapping (`stop_words=None`)**  
   Preserves functional pronouns (*you, your, me, to*). This allows the model to catch predatory structural intent (*"action required by you"*) versus casual conversational use.
3. **Phrase & Syntax Pairing (`ngram_range=(1, 2)`)**  
   Extracts both individual terms (unigrams) and consecutive two-word combinations (bigrams). Legitimate isolated words are caught when paired into malicious strings like `['secure', 'link']`.

---

## 📊 Model Performance

- **Training Accuracy:** `99.2%`
- **Testing Accuracy:** `96.2%`
- **Core Algorithm:** Logistic Regression
- **Text Vectorizer:** TF-IDF Vectorizer with a custom Absolute Tokenizer

---

## 🛠️ Project Structure

```text
├── app.py                  # Main Streamlit web application code
├── Mail_test.pkl           # Trained Logistic Regression model object
├── feature_test.pkl        # Serialized TF-IDF Vectorizer 
├── requirements.txt        # Production Python dependencies
├── mail.png                # App layout graphic asset
└── IMG-20260704-WA0633.jpg # Profile picture asset
```

---

## 🚀 Local Deployment Setup

To run this project on your local machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/bahsulayman689-hash
cd mail_classifier
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit App
```bash
streamlit run app.py
```

---

## 📦 Cloud Deployment (Streamlit Community Cloud)

1. Push this entire repository (including `.pkl` files and image assets) to your **GitHub** account.
2. Log into [Streamlit Community Cloud](https://streamlit.io).
3. Click **New App**, select this repository, set the main file path to `app.py`, and click **Deploy**.

---

## 👨‍💻 Developer Profile

**Sulayman Bah**  
*Machine Learning & Deep Learning Engineer*  
📍 The Gambia  

- **GitHub:** [@bahsulayman689-hash](https://github.com/bahsulayman689-hash)
- **Portfolio:** [yourportfolio.com](https://yourportfolio.com)

---
*Built with passion for secure, AI-driven applications.*
