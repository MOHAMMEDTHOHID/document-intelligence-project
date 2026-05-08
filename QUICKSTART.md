# 🚀 Quick Start Guide

Get the Document Intelligence Platform running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Quick Setup Steps

### Step 1: Open Command Prompt/Terminal

Navigate to the project folder:
```bash
cd doc_intelligence_platform
```

### Step 2: Create & Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

*If you get errors, try upgrading pip first:*
```bash
python -m pip install --upgrade pip
```

### Step 4: Run the Application

**Easiest Way - Use Main Menu:**
```bash
python main.py
```

Then select option `4` to start both services.

**Or run manually in separate terminals:**

**Terminal 1 (Backend):**
```bash
python -m uvicorn backend.api:app --reload
```

**Terminal 2 (Frontend):**
```bash
streamlit run app/main.py
```

### Step 5: Access the Application

- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## First Time Setup Checklist

- [ ] Python installed (check: `python --version`)
- [ ] Virtual environment created
- [ ] Requirements installed
- [ ] Backend running on port 8000
- [ ] Frontend running on port 8501
- [ ] Can access http://localhost:8501

## Test the Application

1. Go to http://localhost:8501
2. Click "Sign Up"
3. Create account:
   - Email: `test@example.com`
   - Password: `test123456`
4. Upload a text document
5. Try the summarize feature

## Common Commands

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Install new package
pip install package-name

# View installed packages
pip list

# Update requirements
pip freeze > requirements.txt

# Run tests (if available)
pytest

# Check API health
curl http://localhost:8000/health
```

## Project Structure Overview

```
doc_intelligence_platform/
├── main.py              ← Run this to start
├── requirements.txt     ← Dependencies
├── README.md           ← Full documentation
├── app/
│   └── main.py         ← Frontend UI (Streamlit)
├── backend/
│   └── api.py          ← Backend API (FastAPI)
├── utils/
│   ├── document_processor.py
│   ├── ai_generator.py
│   ├── user_manager.py
│   └── auth.py
├── data/               ← Uploaded files
├── outputs/            ← Generated files
└── users/              ← User data
```

## Troubleshooting

### Issue: "Module not found"
```bash
# Make sure venv is activated
# Windows: venv\Scripts\activate.bat
# Mac/Linux: source venv/bin/activate

# Then reinstall requirements
pip install -r requirements.txt
```

### Issue: "Port already in use"
```bash
# Kill process on port 8000 (Backend)
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -i :8000 | grep LISTEN
kill -9 <PID>
```

### Issue: "Frontend not loading"
```bash
# Restart frontend
# Press Ctrl+C in terminal
streamlit run app/main.py

# Or try different port
streamlit run app/main.py --server.port 8502
```

## What's Next?

1. Read [README.md](README.md) for full documentation
2. Explore API at http://localhost:8000/docs
3. Check [API Endpoints](README.md#-api-endpoints) section
4. Integrate your OpenAI API key in `.env`

## Features to Try

- 📤 Upload Documents (PDF, DOCX, TXT)
- 📝 Generate Summaries
- 📋 Generate Notes
- 📧 Generate Emails
- ❓ Ask Questions (Q&A)
- 📚 View History

---

**Stuck? Check the full [README.md](README.md) for detailed help!**
