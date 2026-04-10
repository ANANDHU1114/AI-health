# AI-Powered Health Symptom Checker

A full-stack application that leverages Machine Learning (Random Forest) and Natural Language Processing (TF-IDF) to predict possible diseases from user-submitted symptoms via a premium Chatbot UI. 

## Features
- **Machine Learning**: Predicts diseases from natural text queries with probabilities and offers medical suggestions (precautions, non-prescription meds).
- **FastAPI Backend**: Lightning-fast RESTful APIs and static file generation.
- **Glassmorphism Frontend**: A stunning dark-mode Chatbot UI built purely in HTML, CSS, and vanilla JS.
- **SQLite Database**: Full historical session tracking with a slide-in History Tab.
- **DevOps Ready**: Pre-configured `Dockerfile` and GitHub Actions pipeline.

## Tech Stack
- Frontend: HTML5, CSS3, JavaScript (Vanilla)
- Backend: Python 3.10, FastAPI, SQLite
- ML Model: Scikit-learn (RandomForestClassifier, TfidfVectorizer), Pandas
- Testing & CI: Pytest, GitHub Actions, Docker

## Setup & Running Locally

1. Create a virtual environment and install packages:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Or `venv/bin/activate` on Linux/Mac
   pip install -r requirements.txt
   ```

2. Generate Data and Train the ML Model:
   ```bash
   python data/generate_dataset.py
   python ml_model/train.py
   ```

3. Start the Application:
   ```bash
   uvicorn backend.main:app --reload
   ```

4. Go to `http://127.0.0.1:8000` in your web browser.

## Docker Setup

Build and run via Docker:
```bash
docker build -t ai-symptom-checker .
docker run -p 8000:8000 ai-symptom-checker
```

Explore the Swagger UI documentation at `http://127.0.0.1:8000/docs`.
