import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(135deg, #fef9f3 0%, #fff7ed 50%, #fef6ee 100%);
    color: #334155;
    min-height: 100vh;
}

.main {
    background: transparent;
    padding: 2rem;
}

/* Modern Hero Section */
.hero-section {
    text-align: center;
    padding: 80px 40px 60px;
    background: linear-gradient(135deg, rgba(251, 146, 60, 0.08), rgba(129, 140, 248, 0.05));
    border-radius: 24px;
    margin-bottom: 50px;
    border: 1px solid rgba(251, 146, 60, 0.15);
    backdrop-filter: blur(20px);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(251, 146, 60, 0.08) 0%, transparent 70%);
    animation: pulse 15s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}

.hero-section h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 4.5em;
    font-weight: 700;
    background: linear-gradient(135deg, #fb923c 0%, #f97316 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
    letter-spacing: -2px;
    position: relative;
    z-index: 1;
    text-shadow: 0 0 40px rgba(251, 146, 60, 0.2);
}

.hero-section p {
    font-size: 1.4em;
    color: #64748b;
    margin-bottom: 12px;
    font-weight: 500;
    position: relative;
    z-index: 1;
}

.subtitle {
    color: #94a3b8;
    font-size: 1.1em;
    font-weight: 400;
    position: relative;
    z-index: 1;
}

/* Modern Stats Container */
.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 45px;
    margin: 40px 0 50px;
}

.stat-box {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.9), rgba(254, 249, 243, 0.8));
    border-radius: 20px;
    border: 1px solid rgba(251, 146, 60, 0.2);
    backdrop-filter: blur(10px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.stat-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #fb923c, #818cf8);
    transform: scaleX(0);
    transition: transform 0.4s ease;
}

.stat-box:hover {
    transform: translateY(-8px);
    border-color: rgba(251, 146, 60, 0.4);
    box-shadow: 0 20px 40px rgba(251, 146, 60, 0.15);
}

.stat-box:hover::before {
    transform: scaleX(1);
}

.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8em;
    font-weight: 700;
    background: linear-gradient(135deg, #fb923c, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
}

.stat-label {
    color: #64748b;
    font-size: 1em;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Modern Features Container */
.features-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 45px;
    margin: 50px 0;
}

.feature-box {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(254, 249, 243, 0.9));
    border: 1px solid rgba(251, 146, 60, 0.15);
    border-radius: 20px;
    padding: 35px;
    backdrop-filter: blur(15px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.feature-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(251, 146, 60, 0.05), transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.feature-box:hover {
    border-color: rgba(251, 146, 60, 0.4);
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(251, 146, 60, 0.15);
}

.feature-box:hover::before {
    opacity: 1;
}

.feature-box h3 {
    font-family: 'Space Grotesk', sans-serif;
    color: #fb923c;
    margin-bottom: 15px;
    font-size: 1.4em;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 12px;
}

.feature-box p {
    color: #475569;
    line-height: 1.8;
    font-size: 1em;
    position: relative;
    z-index: 1;
}

.step-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    background: linear-gradient(135deg, #fb923c, #818cf8);
    color: white;
    border-radius: 12px;
    font-weight: 700;
    font-size: 1.2em;
    box-shadow: 0 4px 15px rgba(251, 146, 60, 0.3);
}

/* Modern Divider */
.divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(251, 146, 60, 0.3), transparent);
    margin: 50px 0;
    position: relative;
}

.divider::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 60px;
    height: 60px;
    background: radial-gradient(circle, rgba(251, 146, 60, 0.15), transparent);
    border-radius: 50%;
}

/* Modern Button Styles */
.cta-button {
    display: inline-block;
    margin-top: 40px;
}

.button-text {
    font-size: 1.2em;
    font-weight: 600;
}

/* Section Headers */
h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.5em;
    font-weight: 700;
    color: #334155;
    margin-bottom: 40px;
    text-align: center;
}

/* Animation for elements */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-section, .stat-box, .feature-box {
    animation: fadeInUp 0.8s ease-out;
}

.stat-box:nth-child(2) { animation-delay: 0.1s; }
.stat-box:nth-child(3) { animation-delay: 0.2s; }
.feature-box:nth-child(2) { animation-delay: 0.1s; }
.feature-box:nth-child(3) { animation-delay: 0.2s; }
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
st.markdown("<h2 style='text-align: center; color: #334155; margin-bottom: 30px;'>⚙️ How It Works</h2>", unsafe_allow_html=True)

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
st.markdown("<h2 style='text-align: center; color: #334155; margin-bottom: 30px;'>🎯 Why This Matters</h2>", unsafe_allow_html=True)

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
    height: 60px !important;
    font-size: 1.2em !important;
    font-weight: 600 !important;
    background: linear-gradient(135deg, #fb923c, #818cf8) !important;
    border: none !important;
    border-radius: 12px !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(251, 146, 60, 0.3) !important;
    transition: all 0.3s ease !important;
}

button[key="cta_button"]:hover {
    background: linear-gradient(135deg, #f97316, #6366f1) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(251, 146, 60, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)