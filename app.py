import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="wide")

st.markdown("""
<style>
* {
    margin: 0;
    padding: 0;
}

body {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.main {
    background: transparent;
}

.hero-section {
    text-align: center;
    padding: 60px 20px 40px;
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8));
    border-radius: 20px;
    margin-bottom: 40px;
    border: 1px solid rgba(148, 163, 184, 0.2);
    backdrop-filter: blur(10px);
}

.hero-section h1 {
    font-size: 3.5em;
    font-weight: 800;
    background: linear-gradient(135deg, #60a5fa, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 15px;
    letter-spacing: -1px;
}

.hero-section p {
    font-size: 1.2em;
    color: #cbd5e1;
    margin-bottom: 10px;
    font-weight: 500;
}

.subtitle {
    color: #94a3b8;
    font-size: 1em;
}

.features-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin: 40px 0;
}

.feature-box {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.5));
    border: 1px solid rgba(148, 163, 184, 0.3);
    border-radius: 16px;
    padding: 30px;
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
}

.feature-box:hover {
    border-color: rgba(96, 165, 250, 0.5);
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
    transform: translateY(-5px);
}

.feature-box h3 {
    color: #60a5fa;
    margin-bottom: 12px;
    font-size: 1.3em;
}

.feature-box p {
    color: #cbd5e1;
    line-height: 1.6;
    font-size: 0.95em;
}

.step-number {
    display: inline-block;
    width: 35px;
    height: 35px;
    background: linear-gradient(135deg, #60a5fa, #3b82f6);
    color: white;
    border-radius: 50%;
    text-align: center;
    line-height: 35px;
    font-weight: bold;
    margin-right: 10px;
}

.cta-button {
    display: inline-block;
    margin-top: 30px;
}

.button-text {
    font-size: 1.1em;
    font-weight: 600;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.3), transparent);
    margin: 40px 0;
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin: 30px 0 40px;
}

.stat-box {
    text-align: center;
    padding: 20px;
    background: rgba(30, 41, 59, 0.4);
    border-radius: 12px;
    border: 1px solid rgba(96, 165, 250, 0.2);
}

.stat-number {
    font-size: 2em;
    font-weight: 700;
    color: #60a5fa;
}

.stat-label {
    color: #94a3b8;
    font-size: 0.9em;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>📰 Fake News Detector</h1>
    <p>AI-Powered News Credibility Checker</p>
    <p class="subtitle">Detect misinformation in seconds with advanced machine learning</p>
</div>
""", unsafe_allow_html=True)

# Stats
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">98%</div>
        <div class="stat-label">Accuracy Rate</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">&lt;1s</div>
        <div class="stat-label">Detection Time</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">AI</div>
        <div class="stat-label">Powered</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# How It Works
st.markdown("<h2 style='text-align: center; color: #e2e8f0; margin-bottom: 30px;'>⚙️ How It Works</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="features-container">
    <div class="feature-box">
        <h3><span class="step-number">1</span>Input</h3>
        <p>Paste a news article or claim you want to verify. Our system accepts text of any length.</p>
    </div>
    <div class="feature-box">
        <h3><span class="step-number">2</span>Process</h3>
        <p>Text is cleaned and vectorized using <strong>TF-IDF</strong> technology for accurate analysis.</p>
    </div>
    <div class="feature-box">
        <h3><span class="step-number">3</span>Classify</h3>
        <p><strong>Logistic Regression</strong> model classifies content as Fake or Real with confidence scores.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Why It Matters
st.markdown("<h2 style='text-align: center; color: #e2e8f0; margin-bottom: 30px;'>🎯 Why This Matters</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
    <div class="feature-box">
        <h3>🔴 The Problem</h3>
        <p>Fake news spreads rapidly, distorts public perception, and causes real-world harm. Traditional fact-checking is too slow.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <h3>🟢 Our Solution</h3>
        <p>Instant credibility assessment powered by AI. Get reliable analysis in seconds to combat misinformation effectively.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# CTA Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Start Detecting Now", use_container_width=True, key="cta_button"):
        st.switch_page("pages/1_Detector.py")

st.markdown("""
<style>
button[key="cta_button"] {
    height: 50px !important;
    font-size: 1.1em !important;
    background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
    border: none !important;
    border-radius: 10px !important;
}

button[key="cta_button"]:hover {
    background: linear-gradient(135deg, #2563eb, #1e40af) !important;
}
</style>
""", unsafe_allow_html=True)