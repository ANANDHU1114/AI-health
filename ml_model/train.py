import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import json
import os

def train():
    print("Loading dataset...")
    # Load dataset
    df = pd.read_csv('d:/devops proj/data/symptom_dataset.csv')
    
    # Feature & Target
    X_text = df['Symptoms']
    y = df['Disease']
    
    # Extract unique disease info for suggestions
    disease_info = {}
    for _, row in df.drop_duplicates(subset=['Disease']).iterrows():
        disease_info[row['Disease']] = {
            "Description": row['Description'],
            "Precautions": row['Precautions'],
            "Medications": row['Medications'],
            "Doctor_Recommendation": row['Doctor_Recommendation']
        }
        
    print("Vectorizing data...")
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(X_text)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict & Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Training Complete! Accuracy: {acc:.4f}")
    
    # Save artifacts
    print("Saving model and artifacts...")
    os.makedirs('d:/devops proj/ml_model', exist_ok=True)
    joblib.dump(model, 'd:/devops proj/ml_model/model.joblib')
    joblib.dump(vectorizer, 'd:/devops proj/ml_model/vectorizer.joblib')
    joblib.dump(disease_info, 'd:/devops proj/ml_model/disease_info.joblib')
    print("Saved to /ml_model/ successfully.")

if __name__ == '__main__':
    train()
