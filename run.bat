@echo off
REM Batch file to run the Health Symptom Checker (Frontend + Backend)
REM This script starts the FastAPI backend which serves both the API and frontend

setlocal enabledelayedexpansion

echo ======================================
echo AI Health Symptom Checker - Startup
echo ======================================
echo.

REM Change to project directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists, if not create it
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call "venv\Scripts\activate.bat"
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install/Update dependencies
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

REM Start the backend (serves frontend + API)
echo.
echo Starting FastAPI Backend Server...
echo Backend will serve both API and Frontend
echo.
echo ======================================
echo Access the application at: http://localhost:8000
echo ======================================
echo.

uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

pause
