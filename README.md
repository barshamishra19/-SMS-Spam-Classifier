
# 📩 SMS Spam Classifier 🚀

An AI-powered web application that classifies SMS/Email messages as **Spam 🚨** or **Not Spam ✅** using Machine Learning.

---

## 🚀 Live Demo
🔗 https://hpd56qcy6ugqsrndacpvfu.streamlit.app
---

## 📌 Features
- 📩 Detects Spam vs Not Spam messages
- ⚡ Real-time prediction using Streamlit
- 🧠 Uses TF-IDF Vectorization + Machine Learning Model
- 🧹 Text preprocessing (tokenization, stopword removal, stemming)
- 💻 Clean and interactive UI

---

## 🧠 Tech Stack
- **Frontend**: Streamlit  
- **Backend**: Python  
- **ML Model**: Scikit-learn  
- **NLP**: NLTK  

---

## ⚙️ How It Works
1. User enters a message  
2. Text is preprocessed:
   - Lowercasing  
   - Tokenization  
   - Removing stopwords & punctuation  
   - Stemming  
3. Text is converted into numerical form using **TF-IDF Vectorizer**  
4. Machine Learning model predicts whether it's spam or not  

---

## 📂 Project Structure
SMS-Spam-Classifier/
│
├── app.py                 # Streamlit app
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Dependencies
└── notebooks/
    └── sms-spam-detection.ipynb

---

## 🛠️ Installation & Setup

### 1. Clone the repository
git clone https://github.com/barshamishra19/-SMS-Spam-Classifier
cd -SMS-Spam-Classifier  

### 2. Install dependencies
pip install -r requirements.txt  

### 3. Run the app
streamlit run app.py  

---

## 🧪 Example Test Cases

### 🚨 Spam
- "Congratulations! You won a free lottery. Claim now!"
- "URGENT! Click this link to verify your account"

### ✅ Not Spam
- "Hey, are we meeting tomorrow?"
- "Please send me the notes"

---

## 📈 Future Improvements
- 📊 Show prediction probability  
- 🌙 Dark mode UI  
- 📱 Mobile-friendly design  
- 🔍 Explain why a message is spam  
- 🔗 Extend to phishing URL detection  

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 👩‍💻 Author
**Barsha Mishra**

---

⭐ If you like this project, don’t forget to star the repo!
