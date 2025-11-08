# model/mobilenet_model.py
import tensorflow as tf
import numpy as np
from PIL import Image
import streamlit as st

# Global model variable for caching
_model = None

@st.cache_resource
def load_model():
    """Load MobileNetV2 model with ImageNet weights for feature extraction."""
    model = tf.keras.applications.MobileNetV2(
        weights="imagenet",
        input_shape=(224, 224, 3),
        include_top=True
    )
    return model

def get_model():
    """Get or load the model (with caching)."""
    global _model
    if _model is None:
        _model = load_model()
    return _model

def predict_image(uploaded_file):
    """
    Analyze medical image and return risk assessment.
    
    Args:
        uploaded_file: Uploaded image file
        
    Returns:
        tuple: (risk_level, recommendation, educational_note, confidence)
    """
    try:
        # Load and preprocess image
        img = Image.open(uploaded_file)
        # Convert RGBA to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Get model predictions
        model = get_model()
        preds = model.predict(img_array, verbose=0)
        
        # Decode top 3 predictions
        decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]
        
        # Extract predictions
        top_prediction = decoded[0][1].lower()
        confidence = float(decoded[0][2])
        
        # Medical risk assessment based on ImageNet categories
        # High-risk indicators
        high_risk_terms = [
            "infection", "wound", "rash", "ulcer", "abscess", "lesion",
            "blister", "eruption", "dermatitis", "eczema", "boil"
        ]
        
        # Medium-risk indicators
        medium_risk_terms = [
            "bruise", "swelling", "inflammation", "sore", "cut", "scratch"
        ]
        
        # Analyze predictions
        all_predictions = " ".join([pred[1].lower() for pred in decoded])
        
        if any(term in all_predictions for term in high_risk_terms):
            risk = "High"
            recommendation = "Visit a healthcare provider as soon as possible. This may require immediate medical attention."
            educational_note = "Skin infections and rashes can indicate various conditions. Early medical intervention is important."
        elif any(term in all_predictions for term in medium_risk_terms):
            risk = "Medium"
            recommendation = "Monitor the condition closely. Consider visiting a clinic within 24-48 hours if it worsens."
            educational_note = "Keep the area clean and avoid scratching. Watch for signs of infection like increased redness or pus."
        else:
            risk = "Low"
            recommendation = "Monitor your symptoms and stay alert for changes. Maintain good hygiene."
            educational_note = "Continue monitoring. If symptoms persist or worsen, consult a healthcare professional."
        
        return risk, recommendation, educational_note, confidence
        
    except Exception as e:
        # Fallback in case of errors
        return "Unknown", "Please try again or consult a healthcare professional directly.", "An error occurred during image analysis.", 0.0
