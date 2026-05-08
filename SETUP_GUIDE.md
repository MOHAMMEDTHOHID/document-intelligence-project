# 📖 Complete Setup & Installation Guide

This guide will walk you through every step to get the Document Intelligence Platform running.

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Windows Setup](#windows-setup)
3. [Mac Setup](#mac-setup)
4. [Linux Setup](#linux-setup)
5. [Verification](#verification)
6. [Running the Application](#running-the-application)
7. [Verification Steps](#verification-steps)

---

## System Requirements

- **Python**: 3.8 or higher
- **Memory**: 2GB RAM minimum
- **Disk Space**: 500MB free
- **Internet**: Required for API calls

### Check Your Python Installation

```bash
python --version
```

Should show Python 3.8 or higher. If not, download from https://www.python.org

---

## Windows Setup

### Step 1: Download the Project

1. Extract the project folder
2. Open Command Prompt or PowerShell
3. Navigate to the folder:

```cmd
cd C:\path\to\doc_intelligence_platform
```

### Step 2: Create Virtual Environment

**Using PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Using Command Prompt:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**You should see `(venv)` at the start of the command line.**

### Step 3: Upgrade pip

```cmd
python -m pip install --upgrade pip
```

### Step 4: Install Requirements

```cmd
pip install -r requirements.txt
```

**This will take 2-5 minutes. Wait for it to complete.**

### Step 5: Create Configuration

```cmd
copy .env.example .env
```

Then edit `.env` with Notepad:
- Add your OpenAI API key
- Change SECRET_KEY to something random

### Step 6: Test Installation

```cmd
python test_installation.py
```

**Should show all tests passing.**

### Step 7: Run the Application

**Using the main menu:**
```cmd
python main.py
```

Then select option `4` to start both services.

**Or manually:**

Terminal 1:
```cmd
python -m uvicorn backend.api:app --reload
```

Terminal 2:
```cmd
streamlit run app/main.py
```

---

## Mac Setup

### Step 1: Download the Project

```bash
cd /path/to/doc_intelligence_platform
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

**You should see `(venv)` at the start of the prompt.**

### Step 3: Upgrade pip

```bash
python3 -m pip install --upgrade pip
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Create Configuration

```bash
cp .env.example .env
```

Edit `.env` with your favorite editor:
```bash
nano .env
# or
vim .env
```

### Step 6: Test Installation

```bash
python3 test_installation.py
```

### Step 7: Run the Application

**Using the main menu:**
```bash
python3 main.py
```

**Or manually:**

Terminal 1:
```bash
python3 -m uvicorn backend.api:app --reload
```

Terminal 2:
```bash
streamlit run app/main.py
```

---

## Linux Setup

### Step 1: Install Dependencies (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
```

### Step 2: Create Virtual Environment

```bash
cd /path/to/doc_intelligence_platform
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Upgrade pip

```bash
python3 -m pip install --upgrade pip
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Create Configuration

```bash
cp .env.example .env
nano .env
```

### Step 6: Test Installation

```bash
python3 test_installation.py
```

### Step 7: Run the Application

Terminal 1:
```bash
python3 -m uvicorn backend.api:app --reload
```

Terminal 2:
```bash
streamlit run app/main.py
```

---

## Verification

### Verify Project Structure

Check that these files exist:

```
doc_intelligence_platform/
├── main.py                    ✓
├── requirements.txt           ✓
├── test_installation.py       ✓
├── README.md                  ✓
├── QUICKSTART.md             ✓
├── app/
│   ├── __init__.py           ✓
│   └── main.py               ✓
├── backend/
│   ├── __init__.py           ✓
│   └── api.py                ✓
├── utils/
│   ├── __init__.py           ✓
│   ├── auth.py               ✓
│   ├── ai_generator.py       ✓
│   ├── document_processor.py ✓
│   └── user_manager.py       ✓
├── data/                      ✓
├── outputs/                   ✓
├── users/                     ✓
└── embeddings/               ✓
```

### Verify Python Packages

After installing requirements, check:

```bash
pip list
```

Should include:
- fastapi
- streamlit
- uvicorn
- PyPDF2
- python-docx
- And others from requirements.txt

### Run Installation Test

```bash
# Windows
python test_installation.py

# Mac/Linux
python3 test_installation.py
```

---

## Running the Application

### Method 1: Automatic (Recommended)

```bash
python main.py
```

Menu:
```
1. Install requirements
2. Start Backend API only
3. Start Frontend only
4. Start both Backend & Frontend  ← Select this
5. Run tests
6. Exit
```

### Method 2: Manual (Two Terminals)

**Terminal 1 - Backend:**
```bash
python -m uvicorn backend.api:app --reload
```

Wait for: "Application startup complete"

**Terminal 2 - Frontend:**
```bash
streamlit run app/main.py
```

Should open browser automatically.

---

## Verification Steps

### 1. Check Backend is Running

```bash
curl http://localhost:8000/health
```

Should return: `{"status":"ok"}`

### 2. Check Frontend is Running

Visit: http://localhost:8501

Should show login page.

### 3. Test API Documentation

Visit: http://localhost:8000/docs

Should show interactive API docs.

### 4. Create Test Account

1. Go to http://localhost:8501
2. Click "Sign Up"
3. Enter:
   - Email: test@test.com
   - Password: test123456
4. Click "Sign Up"

### 5. Test Upload Feature

1. Login with test account
2. Go to "Upload Document"
3. Upload a text file
4. Click "Process Document"
5. Should show character count

### 6. Test Summary Generation

1. Go to "Summarize"
2. Click "Generate Summary"
3. Should show a summary

---

## Troubleshooting

### Issue: Python not found

```bash
# Windows - Check python is installed
python --version

# Mac/Linux
python3 --version

# Add Python to PATH if needed
# Windows: https://www.python.org/downloads/
```

### Issue: Virtual environment not activating

```bash
# Windows - Try:
.\venv\Scripts\Activate.ps1

# If you get permission error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
```

### Issue: Requirements installation fails

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try installing again
pip install -r requirements.txt

# If specific package fails, install individually
pip install fastapi uvicorn streamlit
```

### Issue: Port 8000 already in use

```bash
# Windows - Find and kill process
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8000
kill -9 <PID>

# Or use different port
python -m uvicorn backend.api:app --reload --port 8001
```

### Issue: Frontend not opening

```bash
# Try opening manually
http://localhost:8501

# If still not working, try different port
streamlit run app/main.py --server.port 8502
```

---

## Next Steps After Setup

1. **Update Configuration**
   - Edit `.env`
   - Add your OpenAI API key
   - Change SECRET_KEY

2. **Explore the Platform**
   - Try uploading a document
   - Generate summaries
   - Ask questions about documents

3. **Read Documentation**
   - [README.md](README.md) - Full documentation
   - [QUICKSTART.md](QUICKSTART.md) - Quick reference

4. **Integrate API**
   - Use `/docs` at http://localhost:8000/docs
   - Test API endpoints
   - Build custom integrations

---

## Getting Help

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) section
2. Run `python test_installation.py`
3. Check terminal output for error messages
4. Verify .env configuration
5. Try reinstalling requirements

---

**Congratulations! You're ready to use the Document Intelligence Platform!**
