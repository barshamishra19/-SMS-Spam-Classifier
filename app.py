import streamlit as st
import pickle
import string
import nltk
import os

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize stemmer once
ps = PorterStemmer()

# ✅ FIX: Setup local nltk_data (important for Streamlit Cloud)
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(nltk_data_path)

# Download required resources
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('punkt_tab', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

# Load stopwords once (optimization)
stop_words = set(stopwords.words('english'))

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    # remove non-alphanumeric words
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # remove stopwords and punctuation
    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    # stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer and model
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Streamlit UI
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

# Prediction button
if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message first")
    else:
        # preprocess input
        transformed_sms = transform_text(input_sms)

        # vectorize
        vector_input = tfidf.transform([transformed_sms])

        # predict
        result = model.predict(vector_input)[0]

        # display result
        if result == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")