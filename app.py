import streamlit as st
import joblib

# Load model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# UI
st.title("📧 Spam Classifier")
st.write("Paste a message below to check if it's spam.")

msg = st.text_area("Enter your message:")

if st.button("Predict"):
    msg_vector = vectorizer.transform([msg])
    result = model.predict(msg_vector)[0]
    st.success("🚨 Spam" if result == 1 else "✅ Not Spam")
