# app.py
import streamlit as st
from model.mobilenet_model import predict_image
from utils.helpers import analyze_symptoms

# Page configuration
st.set_page_config(
    page_title="AI Clinic Buddy",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .team-name {
        text-align: center;
        font-style: italic;
        color: #888;
        margin-bottom: 2rem;
    }
    .risk-high {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #f44336;
    }
    .risk-medium {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ff9800;
    }
    .risk-low {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #4caf50;
    }
    .disclaimer {
        background-color: #fff9c4;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 2px solid #fbc02d;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🩺 AI Clinic Buddy</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Helping community health workers screen patients faster — ethically and efficiently.</p>', unsafe_allow_html=True)
st.markdown('<p class="team-name">By Team "Not Robots" — We build AI that cares for humans.</p>', unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **AI Clinic Buddy** is an AI-powered screening tool designed for rural clinics 
    and community health workers in South Africa.
    
    ### How it works:
    1. Upload a medical image OR describe symptoms
    2. AI analyzes and provides a risk assessment
    3. Get recommendations and next steps
    
    ### Key Features:
    - ✅ Image-based analysis (rashes, wounds, infections)
    - ✅ Text-based symptom assessment
    - ✅ Risk scoring (Low/Medium/High)
    - ✅ Actionable recommendations
    - ✅ Privacy-first design
    
    ### Social Impact:
    - Reduces wait times at clinics
    - Supports early disease detection
    - Empowers health workers
    - Improves healthcare access
    """)
    
    st.markdown("---")
    st.markdown("### 🔒 Privacy & Security")
    st.markdown("""
    - No personal data stored
    - Images processed temporarily
    - Local or secure cloud processing
    - Transparent AI decisions
    """)

# Main content area
st.markdown("---")

# Input selection
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📷 Image Analysis")
    uploaded_file = st.file_uploader(
        "Upload a medical image",
        type=["jpg", "jpeg", "png"],
        help="Upload images of rashes, wounds, eye infections, or skin conditions"
    )
    
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded image", use_container_width=True)
        if st.button("🔍 Analyze Image", type="primary", use_container_width=True):
            with st.spinner("🤖 AI is analyzing the image..."):
                risk, recommendation, educational_note, confidence = predict_image(uploaded_file)
            
            # Display results with styling
            risk_colors = {
                "High": ("🔴", "risk-high", "#f44336"),
                "Medium": ("🟠", "risk-medium", "#ff9800"),
                "Low": ("🟢", "risk-low", "#4caf50"),
                "Low-Medium": ("🟡", "risk-medium", "#ffc107"),
                "Unknown": ("⚪", "risk-low", "#9e9e9e")
            }
            
            emoji, css_class, color = risk_colors.get(risk, ("⚪", "risk-low", "#9e9e9e"))
            
            st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
            st.markdown(f"### {emoji} Risk Level: **{risk}**")
            if confidence > 0:
                st.markdown(f"*Confidence: {confidence:.1%}*")
            st.markdown("---")
            st.markdown(f"**📋 Recommendation:**")
            st.markdown(recommendation)
            st.markdown("---")
            st.markdown(f"**💡 Educational Note:**")
            st.markdown(educational_note)
            st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("📝 Symptom Analysis")
    symptoms = st.text_area(
        "Describe your symptoms:",
        height=200,
        help="Enter symptoms like: fever, cough, headache, rash, etc."
    )
    
    example_symptoms = st.expander("💡 Example symptoms to try:")
    with example_symptoms:
        st.code("""
High risk examples:
- Fever with cough and shortness of breath
- Severe chest pain and difficulty breathing
- Unconsciousness or seizure

Medium risk examples:
- Persistent headache and fatigue
- Sore throat with body aches
- Rash with mild fever

Low risk examples:
- Mild headache
- Runny nose
- General fatigue
        """)
    
    if st.button("🔍 Analyze Symptoms", type="primary", use_container_width=True):
        if not symptoms or len(symptoms.strip()) == 0:
            st.warning("⚠️ Please enter symptoms to analyze.")
        else:
            with st.spinner("🤖 AI is analyzing symptoms..."):
                risk, recommendation, educational_note = analyze_symptoms(symptoms)
            
            # Display results with styling
            risk_colors = {
                "High": ("🔴", "risk-high", "#f44336"),
                "Medium": ("🟠", "risk-medium", "#ff9800"),
                "Low": ("🟢", "risk-low", "#4caf50"),
                "Low-Medium": ("🟡", "risk-medium", "#ffc107")
            }
            
            emoji, css_class, color = risk_colors.get(risk, ("⚪", "risk-low", "#9e9e9e"))
            
            st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
            st.markdown(f"### {emoji} Risk Level: **{risk}**")
            st.markdown("---")
            st.markdown(f"**📋 Recommendation:**")
            st.markdown(recommendation)
            st.markdown("---")
            st.markdown(f"**💡 Educational Note:**")
            st.markdown(educational_note)
            st.markdown('</div>', unsafe_allow_html=True)

# Disclaimer section
st.markdown("---")
st.markdown('<div class="disclaimer">', unsafe_allow_html=True)
st.markdown("""
### ⚠️ Important Disclaimer

**This tool does NOT provide medical diagnoses.** 

AI Clinic Buddy is designed for **early screening and risk assessment only**. It supports community health workers by providing preliminary assessments, but:

- ❌ **NOT a replacement** for professional medical evaluation
- ❌ **NOT a diagnostic tool**
- ✅ **A screening assistant** to help prioritize care
- ✅ **Always consult** qualified healthcare professionals for proper diagnosis and treatment

**In case of emergencies, call emergency services immediately.**
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; padding: 1rem;'>
    <p>Built with ❤️ by Team "Not Robots" for GEW25 AI Driven Innovation Hackathon</p>
    <p>Empowering healthcare workers through ethical AI</p>
</div>
""", unsafe_allow_html=True)
