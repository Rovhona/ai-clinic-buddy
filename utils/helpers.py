# utils/helpers.py

def analyze_symptoms(symptoms):
    """
    Analyze text symptoms and return risk assessment.
    
    Args:
        symptoms: Text description of symptoms
        
    Returns:
        tuple: (risk_level, recommendation, educational_note)
    """
    if not symptoms or len(symptoms.strip()) == 0:
        return "Low", "Please describe your symptoms for analysis.", "Enter detailed symptoms for a better assessment."
    
    text = symptoms.lower()
    
    # High-risk symptom keywords (enhanced with common medical terms)
    high_risk_keywords = [
        # Critical symptoms
        "fever", "high temperature", "cough", "shortness of breath", "difficulty breathing",
        "chest pain", "bleeding", "severe pain", "unconscious", "seizure", "convulsion",
        "cannot breathe", "choking", "severe headache", "stiff neck", "rash with fever",
        "vomiting blood", "blood in stool", "severe dehydration", "severe allergic reaction",
        "anaphylaxis", "heart attack", "stroke", "severe burn", "broken bone", "fracture",
        # Enhanced from medical datasets
        "persistent fever", "high fever", "breathing difficulty", "rapid breathing",
        "chest tightness", "severe cough", "bloody cough", "severe fatigue",
        "severe weakness", "confusion", "loss of consciousness", "severe dizziness",
        "severe nausea", "severe vomiting", "severe diarrhea", "severe abdominal pain",
        "rapid heart rate", "irregular heartbeat", "severe chest pain", "unable to speak"
    ]
    
    # Medium-risk symptom keywords (enhanced)
    medium_risk_keywords = [
        # Common symptoms
        "headache", "fatigue", "persistent pain", "nausea", "vomiting", "diarrhea",
        "dizziness", "weakness", "sore throat", "runny nose", "congestion", "body aches",
        "muscle pain", "joint pain", "swelling", "redness", "itchy", "rash",
        "persistent cough", "mild fever", "chills", "loss of appetite", "sleep problems",
        # Enhanced from medical datasets
        "mild cough", "sneezing", "watery eyes", "mild headache", "mild fatigue",
        "slight fever", "mild body aches", "mild sore throat", "mild congestion",
        "itchy skin", "dry cough", "mild nausea", "mild dizziness", "mild weakness",
        "tiredness", "slight pain", "mild discomfort", "minor swelling"
    ]
    
    # Count risk indicators
    high_count = sum(1 for keyword in high_risk_keywords if keyword in text)
    medium_count = sum(1 for keyword in medium_risk_keywords if keyword in text)
    
    # Enhanced risk assessment with multiple symptom weighting
    if high_count >= 2:
        risk = "High"
        recommendation = "Seek medical attention as soon as possible. Multiple high-risk symptoms detected. This may indicate a serious condition requiring immediate care."
        educational_note = "Multiple high-risk symptoms often indicate serious conditions. Don't delay seeking professional medical help. In emergencies, call emergency services immediately."
    elif high_count > 0:
        risk = "High"
        recommendation = "Seek medical attention as soon as possible. These symptoms may indicate a serious condition that requires immediate care."
        educational_note = "High-risk symptoms often require prompt medical evaluation. Don't delay seeking professional help."
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
