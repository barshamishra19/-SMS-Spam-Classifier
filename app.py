import streamlit as st
import pickle
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize stemmer once
ps = PorterStemmer()

# (IMPORTANT) Download required NLTK data (runs once)
nltk.download('punkt')
nltk.download('stopwords')


# Text preprocessing function (same as training)
def transform_text(text):
    text = text.lower()  # convert to lowercase
    text = nltk.word_tokenize(text)  # tokenize

    y = []
    # remove non-alphanumeric words
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    #  remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    # stemming (convert words to root form)
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Load vectorizer and model (trained .pkl files)
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


#  Streamlit UI
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

#  Prediction button
if st.button('Predict'):

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message first")
    else:
        # 1. preprocess input
        transformed_sms = transform_text(input_sms)

        # 2. convert text to vector
        vector_input = tfidf.transform([transformed_sms])

        # 3. predict
        result = model.predict(vector_input)[0]

        # 4. display result
        if result == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")