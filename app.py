import streamlit as st
import joblib

model=joblib.load('sentiment_model.pkl')
vectorizer=joblib.load('vectorizer.pkl')

st.title("🧠 AI Review Analyzer")
st.write("Type a review below to see if it's Positive or Negative.")

user_text = st.text_input("Enter Review:", "This laptop is amazing")

if st.button("Analyze"):
    # 1. Translate text to numbers
    text_vec = vectorizer.transform([user_text])
    
    # 2. Predict
    prediction = model.predict(text_vec)[0]
    
    # 3. Show Result
    if prediction == "Positive":
        st.success(f"Sentiment: {prediction}")
    else:
        st.error(f"Sentiment: {prediction}")