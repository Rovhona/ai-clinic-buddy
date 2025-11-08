# 🩺 AI Clinic Buddy

**By Team "Not Robots"** — *We build AI that cares for humans.*

## Overview

AI Clinic Buddy is an AI-powered screening tool designed to help community health workers in rural South African clinics quickly assess patient symptoms and images. The tool provides risk assessments and recommendations to support early disease detection and improve healthcare access.

## Problem Statement

Rural clinics in South Africa face critical challenges:
- Shortage of doctors and diagnostic tools
- Long wait times for patients
- Limited resources for early disease detection
- Misdiagnosis due to resource constraints

## Solution

AI Clinic Buddy provides:
- **Image Analysis**: Upload medical images (rashes, wounds, infections) for AI-powered risk assessment
- **Symptom Analysis**: Text-based symptom analysis with comprehensive keyword detection
- **Risk Scoring**: Low/Medium/High risk levels with actionable recommendations
- **Educational Notes**: Helpful information to guide next steps
- **Privacy-First**: No personal data stored, temporary processing only

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: MobileNetV2 (TensorFlow/Keras) for image classification
- **Symptom Analysis**: Rule-based keyword matching with comprehensive medical terms
- **Backend**: Python
- **Hosting**: Streamlit Cloud (recommended) or local deployment

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ai_clinic_buddy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## Usage

### Image Analysis
1. Click on "Upload Image" or use the image uploader
2. Upload a medical image (JPG, PNG, JPEG)
3. Click "Analyze Image"
4. Review the risk assessment and recommendations

### Symptom Analysis
1. Enter symptoms in the text area
2. Click "Analyze Symptoms"
3. Review the risk level and recommendations

## Features

### 🔍 AI-Powered Analysis
- MobileNetV2 pre-trained model for image classification
- Comprehensive symptom keyword database
- Multi-factor risk assessment

### 🎨 User-Friendly Interface
- Clean, professional design
- Color-coded risk indicators
- Educational notes and examples
- Responsive layout

### 🔒 Privacy & Security
- No personal data storage
- Temporary image processing
- Transparent AI decisions
- Secure cloud deployment options

### 🌍 Social Impact
- Reduces wait times at clinics
- Supports early disease detection
- Empowers community health workers
- Improves healthcare access in rural areas

## Ethical Considerations

- **Not a Diagnostic Tool**: AI Clinic Buddy provides screening only, not medical diagnoses
- **Privacy First**: No personal health data is stored
- **Transparency**: Clear disclaimers and educational content
- **Human-Centered**: Designed to support, not replace, healthcare professionals

## Business Model

1. **Free Tier**: Basic screening tool for NGOs and rural clinics
2. **Premium API**: Paid integration for telemedicine startups
3. **Partnerships**: Department of Health, WHO, university medical programs

## Judging Criteria Alignment

### 1. Innovation & Creativity (10 points)
- Novel approach to rural healthcare challenges
- Creative use of AI for screening (not diagnosis)
- Human-centered design philosophy

### 2. Best Use of AI (10 points)
- MobileNetV2 for image classification
- Rule-based symptom analysis with comprehensive medical terms
- Ethical AI implementation with clear disclaimers

### 3. Social Impact (10 points)
- Addresses healthcare access in rural South Africa
- Reduces wait times and misdiagnosis
- Potential to scale and create jobs
- Measurable impact on healthcare outcomes

### 4. Data Insights and Modelling (10 points)
- Leverages pre-trained models for medical image analysis
- Comprehensive symptom keyword database
- Risk scoring algorithm based on medical best practices

### 5. Business Model (10 points)
- Clear market (rural clinics, NGOs, telemedicine)
- Sustainable revenue streams (free tier + premium API)
- Partnership opportunities identified

### 6. Security and Data Privacy (10 points)
- No personal data storage
- Temporary image processing
- Clear privacy policies
- Secure deployment practices

## Team

**Team "Not Robots"**
- Tagline: *We build AI that cares for humans*
- Focus: Human-centered AI for social impact

## Hackathon Submission

### 1-Minute Pitch

> "Hi everyone, we're *Not Robots*, and our project is called *AI Clinic Buddy*. In many South African clinics, patients wait hours or even days before seeing a doctor due to shortages and lack of tools. We built a lightweight AI assistant that helps community health workers screen patients faster. Upload an image or describe symptoms, and our AI gives an instant risk score with simple recommendations — without storing any data or replacing medical judgment. It's fast, ethical, and designed for low-resource settings — a small step toward equal healthcare access for everyone. We believe AI shouldn't replace humans; it should make caring for others easier. That's why we're *Not Robots*."

## Future Enhancements

- [ ] Multi-language support (Zulu, Xhosa, Afrikaans)
- [ ] Integration with local clinic systems
- [ ] Mobile app version
- [ ] Voice input for symptoms
- [ ] Telemedicine integration
- [ ] Training on medical datasets (with proper approvals)

## License

This project is created for the GEW25 AI Driven Innovation Hackathon.

## Contact

For questions or partnerships, please contact Team "Not Robots".

---

**Built with ❤️ for healthcare workers and communities in South Africa**

