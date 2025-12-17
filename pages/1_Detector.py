import streamlit as st
from model import predict

st.set_page_config(page_title="Detect News", layout="wide")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.detector-title {
    font-size: 3em;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
}

.detector-subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 1.1em;
    margin-bottom: 30px;
}

.input-section {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.5));
    border: 2px solid rgba(96, 165, 250, 0.3);
    border-radius: 16px;
    padding: 30px;
    backdrop-filter: blur(10px);
    margin-bottom: 30px;
}

textarea {
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(96, 165, 250, 0.3) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    padding: 15px !important;
}

.result-fake {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(220, 38, 38, 0.15));
    border: 2px solid rgba(239, 68, 68, 0.5);
    border-radius: 16px;
    padding: 40px;
    text-align: center;
}

.result-real {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(22, 163, 74, 0.15));
    border: 2px solid rgba(34, 197, 94, 0.5);
    border-radius: 16px;
    padding: 40px;
    text-align: center;
}

.result-title-fake {
    color: #ef4444;
    font-size: 2em;
    font-weight: 800;
    margin: 20px 0;
}

.result-title-real {
    color: #22c55e;
    font-size: 2em;
    font-weight: 800;
    margin: 20px 0;
}

.confidence-bar {
    background: rgba(0, 0, 0, 0.3);
    border-radius: 10px;
    overflow: hidden;
    height: 12px;
    margin: 20px 0;
}

.bar-fill-fake {
    background: linear-gradient(90deg, #ef4444, #dc2626);
    height: 100%;
    border-radius: 10px;
}

.bar-fill-real {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    height: 100%;
    border-radius: 10px;
}

.confidence-text {
    font-size: 1.3em;
    font-weight: 700;
    margin: 15px 0;
}

.confidence-text-fake {
    color: #ef4444;
}

.confidence-text-real {
    color: #22c55e;
}

.result-desc {
    color: #cbd5e1;
    font-size: 1em;
    margin: 15px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="detector-title">🧠 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="detector-subtitle">Paste an article and let AI analyze its credibility</div>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<label style="color: #e2e8f0; font-weight: 600; font-size: 1.1em; margin-bottom: 15px; display: block;">📝 Paste News Article</label>', unsafe_allow_html=True)
news = st.text_area(
    "article_input",
    height=250,
    placeholder="Paste your news article here...",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

if news and len(news.strip()) > 10:
    with st.spinner("🔍 Analyzing article..."):
        label, prob = predict(news)

    if label == 0:
        st.markdown(f"""
        <div class="result-fake">
            <div style="font-size: 3.5em;">⚠️</div>
            <div class="result-title-fake">FAKE NEWS</div>
            <p class="result-desc">This article appears to contain misinformation or unreliable information.</p>
            <div class="confidence-bar">
                <div class="bar-fill-fake" style="width: {prob[0]*100:.1f}%;"></div>
            </div>
            <div class="confidence-text confidence-text-fake">{prob[0]*100:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-real">
            <div style="font-size: 3.5em;">✅</div>
            <div class="result-title-real">REAL NEWS</div>
            <p class="result-desc">This article appears to be credible and reliable based on our analysis.</p>
            <div class="confidence-bar">
                <div class="bar-fill-real" style="width: {prob[1]*100:.1f}%;"></div>
            </div>
            <div class="confidence-text confidence-text-real">{prob[1]*100:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 **Tip:** This analysis is based on machine learning patterns. Always cross-reference with trusted news sources for critical information.")

elif news and len(news.strip()) <= 10:
    st.warning("📝 Please paste a longer article (at least 10 characters) for accurate analysis.")