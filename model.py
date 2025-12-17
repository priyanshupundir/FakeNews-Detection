import pandas as pd
import re
import string
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w"\d\w"', '', text)
    return text

@st.cache_resource
def load_model():
    fake = pd.read_csv("Fake.csv")
    true = pd.read_csv("true.csv")

    fake["class"] = 0
    true["class"] = 1

    data = pd.concat([fake, true])
    data = data.drop(["title", "subject", "date"], axis=1)
    data["text"] = data["text"].apply(wordopt)

    x = data["text"]
    y = data["class"]

    x_train, _, y_train, _ = train_test_split(x, y, test_size=0.25)

    vectorizer = TfidfVectorizer(max_features=5000)
    x_train_vec = vectorizer.fit_transform(x_train)

    model = LogisticRegression(max_iter=1000)
    model.fit(x_train_vec, y_train)

    return vectorizer, model

def predict(text):
    vectorizer, model = load_model()
    text = wordopt(text)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0], model.predict_proba(vec)[0]