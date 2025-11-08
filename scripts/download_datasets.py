"""
Script to download and prepare Kaggle datasets for AI Clinic Buddy
"""
import os
import sys
import pandas as pd
import json

# Fix Windows encoding for emoji output
try:
    if sys.platform == 'win32':
        # Try to set UTF-8 encoding
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
except:
    # Fallback: will use ASCII-safe characters
    pass

def download_kaggle_dataset(dataset_name, download_path="data"):
    """
    Download a Kaggle dataset.
    
    Args:
        dataset_name: Kaggle dataset name (e.g., 'itachi9604/disease-symptom-description-dataset')
        download_path: Path to save the dataset
    """
    try:
        import kaggle
        from kaggle.api.kaggle_api_extended import KaggleApi
        
        api = KaggleApi()
        api.authenticate()
        
        # Create directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)
        
        # Download dataset
        print(f"Downloading {dataset_name}...")
        api.dataset_download_files(dataset_name, path=download_path, unzip=True)
        print(f"✅ Dataset downloaded to {download_path}")
        
    except ImportError:
        print("❌ Kaggle API not installed. Install with: pip install kaggle")
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        print("\nManual download instructions:")
        print(f"1. Go to https://www.kaggle.com/datasets/{dataset_name}")
        print(f"2. Click 'Download'")
        print(f"3. Extract to {download_path}/")

def process_disease_symptom_dataset(csv_path="data/dataset.csv"):
    """
    Process disease symptom dataset and create enhanced symptom keywords.
    
    Args:
        csv_path: Path to the disease symptom CSV file
    """
    try:
        # Load dataset
        print(f"📖 Reading CSV file: {csv_path}")
        df = pd.read_csv(csv_path)
        
        # Display dataset info
        print(f"\n📊 Dataset loaded: {len(df)} rows, {len(df.columns)} columns")
        print(f"Columns: {list(df.columns)}")
        print("\nFirst few rows:")
        print(df.head())
        
        # Extract symptoms and diseases
        symptoms_list = []
        diseases_list = []
        
        # Try to find symptom and disease columns (case-insensitive)
        df_columns_lower = [col.lower() for col in df.columns]
        
        # Look for symptom column
        symptom_col = None
        for col in df.columns:
            if 'symptom' in col.lower() or 'symptom' in str(df[col].iloc[0] if len(df) > 0 else '').lower():
                symptom_col = col
                break
        
        # Look for disease column
        disease_col = None
        for col in df.columns:
            if 'disease' in col.lower() or 'disease' in str(df[col].iloc[0] if len(df) > 0 else '').lower():
                disease_col = col
                break
        
        # If not found, try common alternative names
        if not symptom_col:
            for alt in ['symptoms', 'symptom_text', 'description', 'text', 'label']:
                if alt in df_columns_lower:
                    symptom_col = df.columns[df_columns_lower.index(alt)]
                    break
        
        if not disease_col:
            for alt in ['disease', 'disease_name', 'condition', 'illness']:
                if alt in df_columns_lower:
                    disease_col = df.columns[df_columns_lower.index(alt)]
                    break
        
        # Extract data
        if symptom_col:
            print(f"\n✅ Found symptom column: '{symptom_col}'")
            symptoms_list = df[symptom_col].dropna().astype(str).tolist()
            # Clean and extract individual symptoms from text
            all_symptoms = []
            for symptom_text in symptoms_list:
                # Split by common delimiters
                if ',' in symptom_text:
                    all_symptoms.extend([s.strip().lower() for s in symptom_text.split(',')])
                elif ';' in symptom_text:
                    all_symptoms.extend([s.strip().lower() for s in symptom_text.split(';')])
                else:
                    all_symptoms.append(symptom_text.strip().lower())
            symptoms_list = list(set(all_symptoms))  # Remove duplicates
        
        if disease_col:
            print(f"✅ Found disease column: '{disease_col}'")
            diseases_list = df[disease_col].dropna().unique().tolist()
        
        # Create enhanced keywords file
        enhanced_keywords = {
            'high_risk_diseases': diseases_list[:30] if diseases_list else [],
            'symptoms': symptoms_list[:100] if symptoms_list else [],
            'total_rows': len(df),
            'source_file': csv_path
        }
        
        # Save to JSON
        output_path = "data/enhanced_symptoms.json"
        os.makedirs("data", exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(enhanced_keywords, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Enhanced symptoms saved to {output_path}")
        print(f"   - {len(enhanced_keywords['symptoms'])} unique symptoms extracted")
        print(f"   - {len(enhanced_keywords['high_risk_diseases'])} diseases found")
        print("\n💡 You can now use this enhanced data in your symptom analyzer!")
        return enhanced_keywords
        
    except FileNotFoundError:
        print(f"❌ File not found: {csv_path}")
        print("Please download the dataset first.")
        print("\nManual download:")
        print("1. Go to https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset")
        print("2. Click 'Download'")
        print("3. Extract CSV to 'data/' folder")
    except Exception as e:
        print(f"❌ Error processing dataset: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🔽 Kaggle Dataset Downloader for AI Clinic Buddy\n")
    
    # Dataset options
    datasets = {
        "1": {
            "name": "itachi9604/disease-symptom-description-dataset",
            "description": "Disease Symptom Dataset (Recommended for symptom analysis)"
        },
        "2": {
            "name": "niyar56/symptom2disease-dataset",
            "description": "Symptom2Disease Dataset (Alternative for symptom analysis)"
        }
    }
    
    print("Available datasets:")
    for key, value in datasets.items():
        print(f"{key}. {value['description']}")
        print(f"   Kaggle: {value['name']}\n")
    
    choice = input("Enter dataset number to download (or 'skip' to process existing data): ")
    
    if choice in datasets:
        dataset_name = datasets[choice]["name"]
        download_kaggle_dataset(dataset_name)
        print("\nProcessing dataset...")
        # Create data directory if it doesn't exist
        data_dir = "data"
        os.makedirs(data_dir, exist_ok=True)
        
        # Try to find the CSV file
        if os.path.exists(data_dir):
            csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
            if csv_files:
                process_disease_symptom_dataset(os.path.join(data_dir, csv_files[0]))
            else:
                print("⚠️ CSV file not found in data/ directory.")
                print("\n💡 Manual download option:")
                print("1. Go to https://www.kaggle.com/datasets/" + dataset_name)
                print("2. Click 'Download' (you need to be logged in)")
                print("3. Extract the CSV file to the 'data/' folder")
                print("4. Run this script again and choose 'skip' to process the file")
        else:
            print(f"⚠️ Could not create {data_dir} directory.")
    elif choice.lower() == 'skip':
        # Process existing data
        print("\n📂 Looking for CSV files in 'data/' directory...")
        data_dir = "data"
        os.makedirs(data_dir, exist_ok=True)
        
        if os.path.exists(data_dir):
            csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
            if csv_files:
                print(f"Found {len(csv_files)} CSV file(s):")
                for i, csv_file in enumerate(csv_files, 1):
                    print(f"  {i}. {csv_file}")
                
                if len(csv_files) == 1:
                    csv_path = os.path.join(data_dir, csv_files[0])
                    print(f"\nProcessing: {csv_path}")
                    process_disease_symptom_dataset(csv_path)
                else:
                    file_choice = input(f"\nEnter file number (1-{len(csv_files)}): ")
                    try:
                        csv_path = os.path.join(data_dir, csv_files[int(file_choice) - 1])
                        process_disease_symptom_dataset(csv_path)
                    except (ValueError, IndexError):
                        print("❌ Invalid file number")
            else:
                csv_path = input("Enter full path to CSV file: ")
                if os.path.exists(csv_path):
                    process_disease_symptom_dataset(csv_path)
                else:
                    print(f"❌ File not found: {csv_path}")
        else:
            csv_path = input("Enter full path to CSV file: ")
            if os.path.exists(csv_path):
                process_disease_symptom_dataset(csv_path)
            else:
                print(f"❌ File not found: {csv_path}")
    else:
        print("❌ Invalid choice")

