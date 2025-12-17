import streamlit as st

def landing_page():
    st.markdown(
        """
        <style>
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        }

        .hero-container {
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8));
            border-radius: 20px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            backdrop-filter: blur(10px);
            margin-bottom: 40px;
        }

        .title {
            font-size: 48px;
            font-weight: 800;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            letter-spacing: -1px;
        }

        .subtitle {
            font-size: 20px;
            color: #cbd5e1;
            font-weight: 500;
            margin-bottom: 8px;
        }

        .tagline {
            font-size: 14px;
            color: #94a3b8;
            margin-top: 5px;
        }

        .workflow-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }

        .workflow-box {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(15, 23, 42, 0.5));
            border: 1px solid rgba(148, 163, 184, 0.3);
            border-radius: 16px;
            padding: 30px;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .workflow-box:hover {
            border-color: rgba(96, 165, 250, 0.5);
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.8));
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(96, 165, 250, 0.1);
        }

        .workflow-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            color: white;
            border-radius: 50%;
            font-weight: bold;
            font-size: 20px;
            margin-bottom: 15px;
        }

        .workflow-title {
            font-size: 18px;
            font-weight: 700;
            color: #60a5fa;
            margin-bottom: 10px;
        }

        .workflow-desc {
            color: #cbd5e1;
            line-height: 1.6;
            font-size: 15px;
        }

        .divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.3), transparent);
            margin: 40px 0;
        }

        .info-box {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(96, 165, 250, 0.05));
            border: 1px solid rgba(96, 165, 250, 0.3);
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }

        .info-label {
            color: #60a5fa;
            font-weight: 600;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }

        .info-content {
            color: #e2e8f0;
            line-height: 1.7;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="title">📰 Fake News Detection</div>
        <div class="subtitle">AI-Powered News Credibility Checker</div>
        <div class="tagline">Instant analysis | Machine learning powered | Real-time results</div>
    </div>
    """, unsafe_allow_html=True)

    # Workflow Steps
    st.markdown("<h2 style='text-align: center; color: #e2e8f0; margin-bottom: 30px;'>How It Works</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="workflow-container">
        <div class="workflow-box">
            <div class="workflow-number">1</div>
            <div class="workflow-title">📝 Input Article</div>
            <div class="workflow-desc">Paste the full news article or text you want to analyze. Our system handles any length of content.</div>
        </div>
        <div class="workflow-box">
            <div class="workflow-number">2</div>
            <div class="workflow-title">🧠 Analyze Patterns</div>
            <div class="workflow-desc">Our ML model examines writing patterns, language structure, and content characteristics.</div>
        </div>
        <div class="workflow-box">
            <div class="workflow-number">3</div>
            <div class="workflow-title">✅ Get Results</div>
            <div class="workflow-desc">Receive instant classification: Fake or Real with confidence scores and detailed insights.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Key Features Info
    st.markdown("""
    <div class="info-box">
        <div class="info-label">✨ Key Features</div>
        <div class="info-content">
            <strong>Fast Detection:</strong> Get results in seconds, not minutes<br>
            <strong>Accurate:</strong> Trained on thousands of verified articles<br>
            <strong>Easy to Use:</strong> Simple copy-paste interface, no technical knowledge required<br>
            <strong>Instant Feedback:</strong> Clear classification with confidence metrics
        </div>
    </div>
    """, unsafe_allow_html=True)