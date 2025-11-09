# 🩺 AI Clinic Buddy


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





