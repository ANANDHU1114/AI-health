from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

from backend.database import init_db
from backend.routes import router

app = FastAPI(title="AI Symptom Checker API")

# Setup CORS just in case
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Database
@app.on_event("startup")
def on_startup():
    init_db()

# Include API routes
app.include_router(router, prefix="/api")

# Mount frontend
app.mount("/", StaticFiles(directory="d:/devops proj/frontend", html=True), name="frontend")
