import streamlit as st
from model import predict

st.set_page_config(page_title="Detect News", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: linear-gradient(135deg, #fef9f3 0%, #fff7ed 50%, #fef6ee 100%);
    color: #334155;
    min-height: 100vh;
}

.detector-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.5em;
    font-weight: 700;
    background: linear-gradient(135deg, #fb923c 0%, #f97316 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 10px;
    text-shadow: 0 0 40px rgba(251, 146, 60, 0.2);
}

.detector-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 1.2em;
    margin-bottom: 50px;
    font-weight: 400;
}

.input-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(254, 249, 243, 0.9));
    border: 2px solid rgba(251, 146, 60, 0.2);
    border-radius: 20px;
    padding: 40px;
    backdrop-filter: blur(15px);
    margin-bottom: 50px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
}

.input-section::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #fb923c, #818cf8);
}

textarea {
    background: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid rgba(251, 146, 60, 0.2) !important;
    border-radius: 16px !important;
    color: #334155 !important;
    padding: 20px !important;
    font-size: 1.1em !important;
    line-height: 1.6 !important;
    transition: all 0.3s ease !important;
}

textarea:focus {
    border-color: rgba(251, 146, 60, 0.5) !important;
    box-shadow: 0 0 20px rgba(251, 146, 60, 0.15) !important;
}

.button-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}

.result-fake {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(220, 38, 38, 0.1));
    border: 2px solid rgba(239, 68, 68, 0.4);
    border-radius: 24px;
    padding: 50px;
    text-align: center;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
    box-shadow: 0 4px 20px rgba(239, 68, 68, 0.1);
    margin-top: 30px;
}

.result-fake::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #ef4444, #dc2626);
}

.result-real {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(22, 163, 74, 0.1));
    border: 2px solid rgba(34, 197, 94, 0.4);
    border-radius: 24px;
    padding: 50px;
    text-align: center;
    backdrop-filter: blur(10px);
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.6s ease-out;
    box-shadow: 0 4px 20px rgba(34, 197, 94, 0.1);
    margin-top: 30px;
}

.result-real::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #22c55e, #16a34a);
}

.result-title-fake {
    font-family: 'Space Grotesk', sans-serif;
    color: #ef4444;
    font-size: 2.5em;
    font-weight: 700;
    margin: 25px 0;
    text-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
}

.result-title-real {
    font-family: 'Space Grotesk', sans-serif;
    color: #22c55e;
    font-size: 2.5em;
    font-weight: 700;
    margin: 25px 0;
    text-shadow: 0 0 30px rgba(34, 197, 94, 0.3);
}

.confidence-bar {
    background: rgba(0, 0, 0, 0.4);
    border-radius: 12px;
    overflow: hidden;
    height: 16px;
    margin: 25px 0;
    position: relative;
}

.bar-fill-fake {
    background: linear-gradient(90deg, #ef4444, #dc2626);
    height: 100%;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}

.bar-fill-fake::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    animation: shimmer 2s infinite;
}

.bar-fill-real {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    height: 100%;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
}

.bar-fill-real::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    animation: shimmer 2s infinite;
}

@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.confidence-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8em;
    font-weight: 700;
    margin: 20px 0;
}

.confidence-text-fake {
    color: #ef4444;
}

.confidence-text-real {
    color: #22c55e;
}

.result-desc {
    color: #475569;
    font-size: 1.1em;
    margin: 20px 0;
    line-height: 1.7;
}

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

button[key="verify_btn"] {
    height: 55px !important;
    font-size: 1.1em !important;
    font-weight: 600 !important;
    background: linear-gradient(135deg, #fb923c, #818cf8) !important;
    border: none !important;
    border-radius: 12px !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(251, 146, 60, 0.3) !important;
    transition: all 0.3s ease !important;
}

button[key="verify_btn"]:hover {
    background: linear-gradient(135deg, #f97316, #6366f1) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(251, 146, 60, 0.4) !important;
}

button[key="back_button"] {
    background: rgba(251, 146, 60, 0.15) !important;
    border: 1px solid rgba(251, 146, 60, 0.3) !important;
    color: #64748b !important;
    border-radius: 8px !important;
    padding: 8px 16px !important;
    font-size: 0.9em !important;
    transition: all 0.3s ease !important;
}

button[key="back_button"]:hover {
    background: rgba(251, 146, 60, 0.25) !important;
    border-color: rgba(251, 146, 60, 0.5) !important;
}
</style>
""", unsafe_allow_html=True)

# Back button
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("← Back", key="back_button"):
        st.switch_page("app.py")

st.markdown('<div style="margin-top: 20px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="detector-title">🧠 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="detector-subtitle">Paste an article and let AI analyze its credibility</div>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
st.markdown('<label style="color: #64748b; font-weight: 600; font-size: 1.2em; margin-bottom: 20px; display: block;">📝 Paste News Article</label>', unsafe_allow_html=True)
news = st.text_area(
    "article_input",
    height=250,
    placeholder="Paste your news article here...",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    verify_button = st.button("🔍 Analyze Article", use_container_width=True, key="verify_btn")

st.markdown('</div>', unsafe_allow_html=True)

if verify_button and news and len(news.strip()) > 10:
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

elif verify_button and news and len(news.strip()) <= 10:
    st.warning("📝 Please paste a longer article (at least 10 characters) for accurate analysis.")

elif verify_button and not news:
    st.error("❌ Please paste an article first before verifying.")