import streamlit as st

st.set_page_config(
    page_title="Fake News Detector",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

/* Hide Streamlit defaults */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Global Styles & Background */
[data-testid="stAppViewContainer"], .main {
    background-color: #FFFBF5;
    font-family: 'Inter', sans-serif;
    color: #334155;
}

/* Sidebar styling to match theme */
[data-testid="stSidebar"] {
    background-color: #FFF4E8 !important;
}

/* Animations */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.animate-up {
    animation: fadeInUp 0.6s ease-out forwards;
}

/* Hero Section */
.hero-card {
    background: linear-gradient(135deg, #FFF4E8 0%, #FFFBF5 100%);
    border-radius: 28px;
    padding: 60px 40px;
    text-align: center;
    box-shadow: 0 2px 20px rgba(0,0,0,0.04);
    margin-bottom: 40px;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 4em;
    font-weight: 700;
    background: linear-gradient(135deg, #F97316, #FB923C, #818CF8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
    line-height: 1.2;
}
.hero-subtitle {
    font-size: 1.5em;
    color: #64748b;
    font-weight: 500;
    margin-bottom: 10px;
}
.hero-tagline {
    font-size: 1.1em;
    color: #94a3b8;
}

/* Stat Cards */
.stat-card {
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 2px 16px rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.04);
    transition: all 0.3s ease;
    height: 100%;
}
.stat-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}
.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8em;
    font-weight: 700;
    margin-bottom: 5px;
}
.stat-label {
    color: #64748b;
    font-size: 0.95em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}
.stat-peach { background-color: #FFF4E8; }
.stat-peach .stat-number { color: #F97316; }

.stat-blue { background-color: #EBF2FF; }
.stat-blue .stat-number { color: #3B82F6; }

.stat-lavender { background-color: #F0EDFF; }
.stat-lavender .stat-number { color: #7C3AED; }

/* Features Container (Grid) */
.features-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
    margin: 40px 0;
}
.feature-card {
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.04);
    border: 1px solid rgba(0,0,0,0.04);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}
.feature-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}
.step-badge {
    width: 45px;
    height: 45px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1.2em;
    margin-bottom: 20px;
}
.card-peach { background-color: #FFF4E8; }
.card-peach .step-badge { background: rgba(249, 115, 22, 0.15); color: #F97316; }
.card-peach h3 { color: #F97316; }

.card-sage { background-color: #E8F5E8; }
.card-sage .step-badge { background: rgba(34, 197, 94, 0.15); color: #22C55E; }
.card-sage h3 { color: #22C55E; }

.card-blue { background-color: #EBF2FF; }
.card-blue .step-badge { background: rgba(59, 130, 246, 0.15); color: #3B82F6; }
.card-blue h3 { color: #3B82F6; }

.feature-card h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4em;
    margin-bottom: 15px;
    font-weight: 700;
}
.feature-card p {
    color: #475569;
    line-height: 1.8;
    margin: 0;
}

/* Full Width Banner */
.banner-card {
    background: linear-gradient(135deg, #FFFBF5 0%, #E0F2FE 50%, #BAE6FD 100%);
    border-radius: 28px;
    padding: 50px;
    margin: 40px 0;
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
.banner-column {
    flex: 1;
    min-width: 300px;
}
.banner-column h3 {
    color: #334155;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5em;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.banner-column p {
    color: #475569;
    line-height: 1.8;
}

/* Subtle Divider */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,0,0,0.06), transparent);
    margin: 40px 0;
    border: none;
}

/* CTA Button */
[data-testid="stButton"] button {
    background: #F97316 !important;
    color: white !important;
    border-radius: 14px !important;
    height: 56px !important;
    font-size: 1.15em !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 14px rgba(249, 115, 22, 0.25) !important;
    border: none !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    max-width: 300px !important;
    margin: 0 auto !important;
    display: block !important;
}
[data-testid="stButton"] button:hover {
    background: #EA580C !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(249, 115, 22, 0.35) !important;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-card animate-up">
    <div class="hero-title">Fake News Detector</div>
    <div class="hero-subtitle">Identify misinformation with AI</div>
    <div class="hero-tagline">Fast, accurate, and reliable news classification.</div>
</div>
""", unsafe_allow_html=True)

# 3 Stat Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="stat-card stat-peach animate-up" style="animation-delay: 0.1s;">
        <div class="stat-number">98%</div>
        <div class="stat-label">Accuracy</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-card stat-blue animate-up" style="animation-delay: 0.2s;">
        <div class="stat-number">&lt;1s</div>
        <div class="stat-label">Detection Time</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-card stat-lavender animate-up" style="animation-delay: 0.3s;">
        <div class="stat-number">AI</div>
        <div class="stat-label">Powered</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# How It Works Section
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="font-family: 'Space Grotesk', sans-serif; color: #334155; font-size: 2.2em;">How It Works</h2>
</div>
<div class="features-container animate-up" style="animation-delay: 0.4s;">
    <div class="feature-card card-peach">
        <div class="step-badge">1</div>
        <h3>Input</h3>
        <p>Paste the text or URL of the news article you want to verify. Our system accepts various formats to make it easy for you.</p>
    </div>
    <div class="feature-card card-sage">
        <div class="step-badge">2</div>
        <h3>Process</h3>
        <p>Our advanced AI engine analyzes the content, checking linguistic patterns, sources, and factual inconsistencies.</p>
    </div>
    <div class="feature-card card-blue">
        <div class="step-badge">3</div>
        <h3>Classify</h3>
        <p>Get instant results showing whether the news is likely Real or Fake, along with confidence scores and insights.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# Why This Matters Section (Full Width Banner)
st.markdown("""
<div class="banner-card animate-up" style="animation-delay: 0.5s;">
    <div class="banner-column">
        <h3>🔴 The Problem</h3>
        <p>Misinformation spreads faster than ever in the digital age. Fake news can manipulate public opinion, damage reputations, and cause widespread panic. It's becoming increasingly difficult for readers to distinguish fact from fiction in their daily news consumption.</p>
    </div>
    <div class="banner-column">
        <h3>🟢 Our Solution</h3>
        <p>We leverage cutting-edge machine learning and natural language processing to combat misinformation. By providing a quick, reliable tool, we empower users to verify the news they consume and share, promoting a healthier digital information ecosystem.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# CTA Button
st.markdown('<div style="text-align: center; margin-bottom: 20px;"><h2 style="font-family: \'Space Grotesk\', sans-serif; color: #334155;">Ready to test it out?</h2></div>', unsafe_allow_html=True)

# Streamlit button wrapped in columns to center it if needed, but CSS handles width and margin auto
col_empty1, col_btn, col_empty2 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Try the Detector Now"):
        st.switch_page("pages/1_Detector.py")