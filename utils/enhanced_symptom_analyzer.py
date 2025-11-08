"""
Enhanced symptom analyzer using Kaggle disease-symptom datasets
"""
import json
import os
from typing import Tuple

# Enhanced keywords from disease-symptom datasets
ENHANCED_KEYWORDS = {
    'high_risk': [
        # Original high-risk keywords
        "fever", "high temperature", "cough", "shortness of breath", "difficulty breathing",
        "chest pain", "bleeding", "severe pain", "unconscious", "seizure", "convulsion",
        "cannot breathe", "choking", "severe headache", "stiff neck", "rash with fever",
        "vomiting blood", "blood in stool", "severe dehydration", "severe allergic reaction",
        "anaphylaxis", "heart attack", "stroke", "severe burn", "broken bone", "fracture",
        # Enhanced from disease datasets
        "persistent fever", "high fever", "breathing difficulty", "rapid breathing",
        "chest tightness", "severe cough", "bloody cough", "severe fatigue",
        "severe weakness", "confusion", "loss of consciousness", "severe dizziness",
        "severe nausea", "severe vomiting", "severe diarrhea", "severe abdominal pain"
    ],
    'medium_risk': [
        # Original medium-risk keywords
        "headache", "fatigue", "persistent pain", "nausea", "vomiting", "diarrhea",
        "dizziness", "weakness", "sore throat", "runny nose", "congestion", "body aches",
        "muscle pain", "joint pain", "swelling", "redness", "itchy", "rash",
        "persistent cough", "mild fever", "chills", "loss of appetite", "sleep problems",
        # Enhanced from disease datasets
        "mild cough", "sneezing", "watery eyes", "mild headache", "mild fatigue",
        "slight fever", "mild body aches", "mild sore throat", "mild congestion",
        "itchy skin", "dry cough", "mild nausea", "mild dizziness", "mild weakness"
    ]
}

def load_enhanced_keywords(json_path="data/enhanced_symptoms.json"):
    """
    Load enhanced keywords from JSON file if available.
    
    Args:
        json_path: Path to enhanced symptoms JSON file
        
    Returns:
        dict: Enhanced keywords dictionary
    """
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r') as f:
                enhanced_data = json.load(f)
                # Merge with existing keywords
                if 'symptoms' in enhanced_data:
                    # Add new symptoms to medium risk (can be refined)
                    ENHANCED_KEYWORDS['medium_risk'].extend(enhanced_data['symptoms'][:20])
                return ENHANCED_KEYWORDS
        except Exception as e:
            print(f"⚠️ Could not load enhanced keywords: {e}")
    
    return ENHANCED_KEYWORDS

def analyze_symptoms_enhanced(symptoms: str, use_dataset: bool = True) -> Tuple[str, str, str]:
    """
    Enhanced symptom analysis with optional dataset integration.
    
    Args:
        symptoms: Text description of symptoms
        use_dataset: Whether to use enhanced keywords from dataset
        
    Returns:
        tuple: (risk_level, recommendation, educational_note)
    """
    if not symptoms or len(symptoms.strip()) == 0:
        return "Low", "Please describe your symptoms for analysis.", "Enter detailed symptoms for a better assessment."
    
    # Load enhanced keywords if available
    if use_dataset:
        keywords = load_enhanced_keywords()
    else:
        keywords = ENHANCED_KEYWORDS
    
    text = symptoms.lower()
    
    # Count risk indicators
    high_count = sum(1 for keyword in keywords['high_risk'] if keyword in text)
    medium_count = sum(1 for keyword in keywords['medium_risk'] if keyword in text)
    
    # Enhanced risk assessment
    if high_count >= 2:
        risk = "High"
        recommendation = "Seek medical attention as soon as possible. Multiple high-risk symptoms detected. This may indicate a serious condition requiring immediate care."
        educational_note = "Multiple high-risk symptoms often indicate serious conditions. Don't delay seeking professional medical help. In emergencies, call emergency services immediately."
    elif high_count > 0:
        risk = "High"
        recommendation = "Seek medical attention as soon as possible. These symptoms may indicate a serious condition that requires immediate care."
        educational_note = "High-risk symptoms often require prompt medical evaluation. Don't delay seeking professional help."
    elif medium_count >= 3:
        risk = "Medium"
        recommendation = "Monitor your symptoms closely. Consider visiting a clinic within 24-48 hours if symptoms persist or worsen. Rest and stay hydrated."
        educational_note = "Multiple symptoms that persist may require medical attention. Rest, stay hydrated, and monitor your condition. If symptoms don't improve, seek medical advice."
    elif medium_count >= 2:
        risk = "Medium"
        recommendation = "Monitor your symptoms closely. Consider visiting a clinic within 24-48 hours if symptoms persist or worsen."
        educational_note = "Rest, stay hydrated, and monitor your condition. If symptoms don't improve, seek medical advice."
    elif medium_count == 1:
        risk = "Low-Medium"
        recommendation = "Monitor symptoms and rest. Visit a clinic if symptoms worsen or persist for more than a few days."
        educational_note = "Many symptoms resolve on their own with rest and hydration. Keep track of any changes."
    else:
        risk = "Low"
        recommendation = "Continue monitoring. Maintain good hygiene, stay hydrated, and rest. Consult a healthcare professional if symptoms persist."
        educational_note = "General wellness practices can help. If symptoms persist or concern you, don't hesitate to seek medical advice."
    
    return risk, recommendation, educational_note

# For backward compatibility
def analyze_symptoms(symptoms: str) -> Tuple[str, str, str]:
    """Backward compatible function."""
    return analyze_symptoms_enhanced(symptoms, use_dataset=True)

