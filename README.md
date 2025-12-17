📰 Fake News Detection using Machine Learning

A Machine Learning–based Fake News Detection system that classifies news articles as Real or Fake using Natural Language Processing (NLP).
The application is built with Streamlit and deployed on Streamlit Community Cloud.

🚀 Live Demo

🔗 Streamlit App:
https://fake-news-ai-detector.streamlit.app/

✨ Features

🧠 Fake vs Real news classification

📄 Accepts full news articles

⚡ Interactive Streamlit interface

📊 NLP-based text analysis

☁️ Cloud-hosted using Streamlit

🛠️ Tech Stack

Language: Python

Frontend: Streamlit

ML Model: Scikit-learn

NLP: TF-IDF Vectorizer

Libraries: Pandas, NumPy

📁 Project Structure
FakeNews-Detection/
│
├── app.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
│
├── pages/
│   └── 1_Detector.py
│
└── README.md

🧠 How It Works

User enters a news article

Text is preprocessed and cleaned

TF-IDF converts text into numerical features

ML model predicts:

🟢 Real News

🔴 Fake News

📰 Example Input

Article:

A group of unnamed scientists claim that drinking hot water every 15 minutes can kill viruses instantly without vaccines.

Prediction: ❌ Fake News

⚙️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/FakeNews-Detection.git
cd FakeNews-Detection

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

☁️ Deployment

This project is deployed using Streamlit Community Cloud, which directly runs the app from the GitHub repository.

🔮 Future Improvements

🤖 Transformer-based models (BERT)

🌍 Multilingual fake news detection

📊 Confidence score visualization

📰 News source credibility analysis

👨‍💻 Author

Priyanshu Pundir
🎓 B.Tech Student
💡 Interested in ML, NLP & Web Development
