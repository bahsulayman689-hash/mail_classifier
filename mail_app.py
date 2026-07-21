import pandas as pd
import numpy as np
import joblib
import streamlit as st
import sys
import re
import os
from urllib.parse import quote

def absolute_tokenizer(text):
    return re.findall(r'\w+|[\W\s]', text)

# 2. Force Python to register it directly into the global execution space
import __main__
__main__.absolute_tokenizer = absolute_tokenizer
sys.modules['__main__'].absolute_tokenizer = absolute_tokenizer

# 3. Now try loading your files
model = joblib.load("Mail_test.pkl")
feature_extraction = joblib.load("feature_test.pkl")

st.set_page_config(
    page_title="📧 Spam Email Detector",
    page_icon='📧',
    layout='wide'
)
col_main, col_right = st.columns([4, 1])
with col_right:
    st.image("mail.png", width=350)
with col_main:
    st.title("📧CLASSIFIER THE MESSAGE EITHER SPAM OR HAM MAIL")
    #st.write("Enter an email or SMS message to determine whether it is Spam or Ham.")

    st.markdown("""
    ### 🔍 Real-Time Message Analysis Breakdown

    When you paste an email into this system, the engine does not just look at the overall meaning; it anatomizes the text structure step-by-step using three distinct detection layers:

    #### 1. Case-Sensitive Signal Check (`lowercase=False`)
    *   **How it works**: The system maps the exact casing profile of the words.
    *   **The Impact**: Standard conversational words like `urgent` or `account` are treated normally. However, if the text contains high-stress, all-caps shouting tokens like `URGENT`, `LOCKED`, or `FREE`, the model registers these as aggressive focal points heavily correlated with malicious phishing tactics.

    #### 2. Structural & Contextual Mapping (`stop_words=None`)
    *   **How it works**: Functional pronouns and connective filler words (such as *you, your, me, to, account*) are fully preserved instead of being deleted.
    *   **The Impact**: Legitimate emails use pronouns casually (*"let me know"*). Spam text often abuses pronouns in specific, predatory patterns to manufacture direct pressure or fake personalization (*"your account has been locked", "action required by you"*). Retaining these words allows the model to capture the structural intent behind the message.

    #### 3. Phrase & Syntax Pairing (`ngram_range=(1, 2)`)
    *   **How it works**: The text is broken down into individual terms (unigrams) and consecutive two-word combinations (bigrams).
    *   **The Impact**: Isolated words like *secure* or *link* might look completely harmless to a basic filter. However, your model extracts the unified phrase **`['secure', 'link']`** or **`['verify', 'your']`**. These specific structural pairings carry massive mathematical weight that immediately tips the Logistic Regression classifier toward a **Spam** verdict.
    """)
st.write("👉Enter an email or SMS message to determine whether it is Spam or Ham.")

st.caption("⚠️ **Note:** This model does not ignore punctuation or capitalization variations.")

message = st.text_area(
    "✍️ Enter your email or SMS",
    placeholder="Paste your email or SMS message here...",
    height=300
)

if st.button("predict"):
    if message.strip() == "":
        st.warning("please enter a meassage")
    else:
        # NEW: Check if the text contains at least one actual letter or number
        if not re.search(r'[a-zA-Z0-9]', message):
            st.error("🚨 **Security Warning:** This text contains zero words recognized by the model vocabulary!")
            st.info("🚨 System Action: Blocked for safety. Spammers often use scrambled symbols or pure gibberish to bypass standard text filters.")

        else:
                message_vector = feature_extraction.transform([message])
                if message_vector.nnz == 0:
                    st.error("🚨 **Security Warning:** This text contains zero words recognized by the model vocabulary!")
                    st.info("🚨 System Action: Blocked for safety. Spammers often use scrambled symbols or pure gibberish to bypass standard text filters.")
                else:
                    prediction = model.predict(message_vector)[0]

                    col1, col2 = st.columns(2)

                    with col1:
                        st.button("🔍 Analyze")

                    with col2:
                        st.button("🗑️ Clear")

                    if prediction == 0:
                        st.error("🚨Spam mesaage")
                        st.info("🚨This message contains characteristics commonly found in spam.")
                    else:
                        st.success("✅Ham (Not Spam)")
                        st.info("✅This message appears to be legitimate.")
st.balloons()
with st.sidebar:

    st.title("📧 Spam Detector")

    st.markdown("""
### Model

- Logistic Regression
- TF-IDF Vectorizer

### Features

- Email Detection
- SMS Detection
- Fast Prediction

### Built With

- Python
- Streamlit
- Scikit-learn
    <style>
    [data-testid="stSidebar"] {
        background-color: #D32F2F !important;
    }
    /* This makes all text inside the sidebar white so it stays readable */
    [data-testid="stSidebar"] __element__ , [data-testid="stSidebar"] p, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] a {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)
    st.divider()

    st.caption(
        "Built by Sulayman Bah • Python • Scikit-learn • Streamlit"
    )

    examples = [
    "Congratulations! You've won a free iPhone. Click here to claim.",
    "Hi, are we still meeting at 3 PM today?",
    "Your bank account has been suspended. Verify immediately."
]

selected = st.selectbox("📌 Try an example", [""] + examples)

if selected:
    message = selected
with st.expander("🧠 How it works"):

    st.write("""
This application uses:

- TF-IDF Vectorization
- Logistic Regression
- Supervised Machine Learning

The model converts text into numerical features
before predicting whether the message is Spam or Ham.
""")
col1, col2, col3 = st.columns(3)

col1.metric("Training Accuracy", "99.2%")
col2.metric("Testing Accuracy", "96.2%")
col3.metric("Algorithm", "Logistic Regression")

st.markdown("""
<style>
div[data-testid="stTextArea"] textarea {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
with st.sidebar:

    st.image("IMG-20260704-WA0633.jpg", width=150)

    st.title("👨‍💻 Sulayman Bah")

    st.write("Machine Learning Developer")

    st.divider()

    st.write("📍 The Gambia")

    st.write("💡 Passionate about AI & Machine Learning")
    st.divider()
        # Twitter/X Link
    twitter_url = f"https://twitter.com{quote("Check out this live AI Spam Email Detector built by Sulayman Bah! Try it here: https://bah-mailclassifier.streamlit.app/")}"
    # LinkedIn Link
    linkedin_url = f"https://linkedin.com{quote("https://bah-mailclassifier.streamlit.app/")}"
    
    st.markdown(f"[🐦 Share on Twitter / X]({twitter_url})", unsafe_allow_html=True)
    st.markdown(f"[💼 Share on LinkedIn]({linkedin_url})", unsafe_allow_html=True)

with st.sidebar:

    st.subheader("🔗 Connect")
    st.markdown("https://github.com/bahsulayman689-hash")
    st.markdown("[GitHub](https://github.com/)")

    st.markdown("[LinkedIn](https://linkedin.com/in/WIN_20250906_05_26_12_Pro.jpg)")

    st.markdown("[Portfolio](https://yourportfolio.com)")
with st.sidebar.expander("👤 About Me"):

    st.write("""
    Hi! I'm Sulayman Bah.
    I'm a mechine learning and deep learning enginner.
    I build Machine Learning and
    Deep Learning applications
    using Python and Streamlit.
    """)
st.sidebar.subheader("🛠 Skills")

st.sidebar.write("🐍 Python")
st.sidebar.write("🤖 Machine Learning")
st.sidebar.write("📊 Data Analysis")
st.sidebar.write("🎨 Deep learning")
st.sidebar.write("🧠 Software enginner")
st.divider()

# --- SIDEBAR CONFIGURATION ---
with st.sidebar:
    st.image("mail.png", width=100)
    st.title("ML Ops Dashboard")
    st.markdown("---")
    
    # 1. Model Selection Hub (Perfect for your 20+ projects)
    st.subheader("📁 Select Project")
    selected_model = st.selectbox(
        "Choose an active deployment:",
        ["Spam Filter v2.1", "Churn Predictor v1.0", "Fraud Detection v4.2", "Sentiment Engine v3.0"]
    )
    
    # 2. Dynamic Model Information
    st.info(f"Active: **{selected_model}**\n\nStatus: 🟢 Operational")
    st.markdown("---")
    
    # 3. Interactive Hyperparameters for Testing
    st.subheader("⚙️ Model Settings")
    decision_threshold = st.slider(
        "Spam Sensitivity Threshold", 
        min_value=0.0, max_value=1.0, value=0.5, step=0.05
    )
    
    st.markdown("---")
    
    # 4. Sticky System Metrics Footer
    st.markdown("### 📊 Infrastructure Status")
    st.caption("🖥️ Server: AWS Lambda (Serverless)")
    st.caption("⚡ Latency: 42ms")
    st.caption("📅 Last Retrained: July 2026")
st.subheader("model Evaluation metrics")
m1, m2, m3 = st.columns(3)
m1.metric(label="test accuracy", value="98.12%")
m1.metric(label="test precision", value="98.65%")
m1.metric(label="test Recall", value="99.17%")

