import streamlit as st
from model import predict

st.set_page_config(page_title="Detect News", layout="wide")

st.markdown("""
<style>
/* Hide Streamlit defaults */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&display=swap');

/* Page Background */
[data-testid="stAppViewContainer"], .main {
    background-color: #FFFBF5;
    font-family: 'Inter', sans-serif;
}

/* Typography */
.main-title {
    font-family: 'Space Grotesk', sans-serif;
    background: linear-gradient(135deg, #F97316, #FB923C, #818CF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    font-size: 3.5em;
    font-weight: 700;
    margin-bottom: 10px;
    padding-top: 20px;
}
.subtitle {
    color: #64748b;
    text-align: center;
    font-size: 1.2em;
    margin-bottom: 40px;
}
.textarea-label {
    color: #64748b;
    font-weight: 600;
    font-size: 1.15em;
    margin-bottom: 10px;
    display: block;
}

/* Input Card Container (Styling the stTextArea wrapper) */
[data-testid="stTextArea"] {
    background: #FFF4E8;
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.04);
    position: relative;
    overflow: hidden;
    margin-bottom: 20px;
}
[data-testid="stTextArea"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #FB923C, #818CF8);
}

/* Textarea styling */
[data-testid="stTextArea"] textarea {
    background: rgba(255, 255, 255, 0.95);
    border: 2px solid rgba(251, 146, 60, 0.15);
    border-radius: 16px;
    color: #334155;
    padding: 20px;
    font-size: 1.1em;
    transition: all 0.3s ease;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(251, 146, 60, 0.4);
    box-shadow: 0 0 15px rgba(251, 146, 60, 0.1);
}

/* Buttons */
/* Analyze Button */
[data-testid="stButton"] button {
    background: #F97316;
    color: white;
    border-radius: 14px;
    height: 55px;
    font-size: 1.1em;
    font-weight: 600;
    box-shadow: 0 4px 14px rgba(249, 115, 22, 0.25);
    transition: all 0.3s ease;
    border: none;
    width: 100%;
}
[data-testid="stButton"] button:hover {
    background: #EA580C;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.35);
    color: white;
}

/* Back Button targeting specific column */
[data-testid="column"]:first-child [data-testid="stButton"] button {
    background: rgba(251, 146, 60, 0.1);
    border: 1px solid rgba(251, 146, 60, 0.2);
    color: #64748b;
    border-radius: 10px;
    height: 40px;
    box-shadow: none;
    width: auto;
    padding: 0 20px;
}
[data-testid="column"]:first-child [data-testid="stButton"] button:hover {
    background: rgba(251, 146, 60, 0.18);
    transform: none;
    color: #64748b;
}

/* Animations & Results */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.result-card {
    animation: fadeInUp 0.6s ease-out forwards;
    border-radius: 24px;
    padding: 50px;
    position: relative;
    overflow: hidden;
    margin-top: 30px;
    margin-bottom: 20px;
}
.result-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
}
.result-fake {
    background: #FFF0F0;
    border: 2px solid rgba(239, 68, 68, 0.25);
    box-shadow: 0 2px 20px rgba(239, 68, 68, 0.08);
}
.result-fake::before {
    background: linear-gradient(90deg, #EF4444, #DC2626);
}
.result-real {
    background: #F0FFF4;
    border: 2px solid rgba(34, 197, 94, 0.25);
    box-shadow: 0 2px 20px rgba(34, 197, 94, 0.08);
}
.result-real::before {
    background: linear-gradient(90deg, #22C55E, #16A34A);
}
.result-title-fake { color: #EF4444; font-size: 2.2em; font-weight: 700; margin-bottom: 10px; margin-top: 0;}
.result-title-real { color: #22C55E; font-size: 2.2em; font-weight: 700; margin-bottom: 10px; margin-top: 0;}
.result-desc { color: #475569; font-size: 1.1em; margin-bottom: 25px;}
.conf-text-fake { color: #EF4444; font-weight: 600; font-size: 1.2em; text-align: right; margin-bottom: 8px;}
.conf-text-real { color: #22C55E; font-weight: 600; font-size: 1.2em; text-align: right; margin-bottom: 8px;}

.conf-bar-bg {
    background: rgba(0, 0, 0, 0.06);
    height: 14px;
    border-radius: 10px;
    width: 100%;
    overflow: hidden;
    position: relative;
}
.conf-bar-fill-fake {
    background: linear-gradient(90deg, #EF4444, #B91C1C);
    height: 100%;
    border-radius: 10px;
    transition: width 1.2s cubic-bezier(0.1, 0.8, 0.2, 1);
    position: relative;
}
.conf-bar-fill-real {
    background: linear-gradient(90deg, #22C55E, #15803D);
    height: 100%;
    border-radius: 10px;
    transition: width 1.2s cubic-bezier(0.1, 0.8, 0.2, 1);
    position: relative;
}
.shimmer {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    animation: shimmer 2s infinite;
}
@keyframes shimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
</style>
""", unsafe_allow_html=True)

# Top Bar with Back Button
col_back, _ = st.columns([1, 10])
with col_back:
    if st.button("← Back", key="back_btn"):
        st.switch_page("app.py")

# Header
st.markdown('<div class="main-title">🧠 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Paste an article and let AI analyze its credibility</div>', unsafe_allow_html=True)

# Main container for inputs
st.markdown('<span class="textarea-label">📝 Paste News Article</span>', unsafe_allow_html=True)

news = st.text_area("", height=250, placeholder="Paste the news article text here...", label_visibility="collapsed")

# Analyze button
col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
with col_btn_2:
    verify = st.button("Analyze Credibility", key="verify_btn")

if verify:
    if len(news) > 10:
        label, prob = predict(news)
        
        if label == 0: # Fake
            confidence = prob[0] * 100
            st.markdown(f"""
            <div class="result-card result-fake">
                <h3 class="result-title-fake">⚠️ Fake News Detected</h3>
                <p class="result-desc">Our AI model analyzed the linguistic patterns and found high indicators of fabricated content.</p>
                <div class="conf-text-fake">Confidence: {confidence:.1f}%</div>
                <div class="conf-bar-bg">
                    <div class="conf-bar-fill-fake" style="width: {confidence}%">
                        <div class="shimmer"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 Tip: Check multiple reputable sources to verify unexpected or highly emotional news.", icon="ℹ️")
            
        elif label == 1: # Real
            confidence = prob[1] * 100
            st.markdown(f"""
            <div class="result-card result-real">
                <h3 class="result-title-real">✅ Real News</h3>
                <p class="result-desc">The article passes our credibility checks and appears to be genuinely reported news.</p>
                <div class="conf-text-real">Confidence: {confidence:.1f}%</div>
                <div class="conf-bar-bg">
                    <div class="conf-bar-fill-real" style="width: {confidence}%">
                        <div class="shimmer"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.info("💡 Tip: Always consider the context and the date of publication, even for real news.", icon="ℹ️")
            
    elif len(news) > 0 and len(news) <= 10:
        st.warning("⚠️ The text is too short to analyze. Please provide a longer excerpt.")
    else:
        st.error("❌ Please paste an article text to analyze.")