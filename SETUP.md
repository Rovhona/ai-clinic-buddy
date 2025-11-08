# Quick Setup Guide for AI Clinic Buddy

## For Hackathon Demo

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
streamlit run app.py
```

### Step 3: Access the App
Open your browser to `http://localhost:8501`

## Testing the Application

### Image Analysis Test
1. Find a sample image online (medical image, skin condition, etc.)
2. Upload it through the image uploader
3. Click "Analyze Image"
4. Review the risk assessment

### Symptom Analysis Test
Try these example inputs:
- **High Risk**: "Fever with cough and shortness of breath"
- **Medium Risk**: "Persistent headache and fatigue with body aches"
- **Low Risk**: "Mild headache and runny nose"

## For Streamlit Cloud Deployment

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set main file to `app.py`
5. Deploy!

## Troubleshooting

### TensorFlow Installation Issues
If you encounter TensorFlow installation issues:
```bash
pip install tensorflow --upgrade
```

### Memory Issues
MobileNetV2 is lightweight, but if you have memory constraints:
- Close other applications
- Use a smaller batch size (already set to 1)

### Model Download
The first run will download MobileNetV2 weights (~14MB). This happens automatically.

## Demo Tips for Hackathon

1. **Have test images ready**: Prepare 2-3 medical images (skin conditions, rashes) for live demo
2. **Test symptom examples**: Practice with different symptom combinations
3. **Highlight features**: 
   - Show the clean UI
   - Demonstrate both image and text analysis
   - Emphasize privacy (no data stored)
   - Show the educational notes

## Presentation Flow

1. Problem statement (30 seconds)
2. Live demo (1-2 minutes)
3. Technical overview (30 seconds)
4. Social impact (30 seconds)
5. Q&A

Good luck! 🚀

