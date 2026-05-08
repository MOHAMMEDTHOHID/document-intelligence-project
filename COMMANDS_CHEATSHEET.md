# 📋 Commands Cheat Sheet

Quick reference for all important commands.

## Setup Commands

### Create Virtual Environment

```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows Command Prompt
python -m venv venv
venv\Scripts\activate.bat

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Activate Virtual Environment

```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat

# Mac/Linux
source venv/bin/activate
```

### Deactivate Virtual Environment

```bash
deactivate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Running the Application

### Option 1: Use Main Menu

```bash
python main.py
```

Then select option `4`

### Option 2: Backend Only

```bash
python -m uvicorn backend.api:app --reload
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Option 3: Frontend Only

```bash
streamlit run app/main.py
# App: http://localhost:8501
```

### Option 4: Both (Separate Terminals)

**Terminal 1:**
```bash
python -m uvicorn backend.api:app --reload
```

**Terminal 2:**
```bash
streamlit run app/main.py
```

### Run on Different Port

```bash
# Backend on port 8001
python -m uvicorn backend.api:app --reload --port 8001

# Frontend on port 8502
streamlit run app/main.py --server.port 8502
```

---

## Testing Commands

### Test Installation

```bash
python test_installation.py
```

### Test API Health

```bash
curl http://localhost:8000/health
```

### Test Endpoints with curl

```bash
# Signup
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"

# Login
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"

# Health check
curl http://localhost:8000/health
```

---

## Port Management

### Find Process Using Port

```bash
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000
```

### Kill Process on Port

```bash
# Windows
taskkill /PID <PID> /F

# Mac/Linux
kill -9 <PID>
```

### Kill All Python Processes

```bash
# Windows
Get-Process python | Stop-Process -Force

# Mac/Linux
killall python
```

---

## Package Management

### List Installed Packages

```bash
pip list
```

### Install Specific Package

```bash
pip install package-name
```

### Install Package with Version

```bash
pip install package-name==1.0.0
```

### Update Package

```bash
pip install --upgrade package-name
```

### Uninstall Package

```bash
pip uninstall package-name
```

### Update Requirements File

```bash
pip freeze > requirements.txt
```

---

## File Management

### Create .env File from Template

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

### Edit .env File

```bash
# Windows
notepad .env

# Mac/Linux
nano .env
# or
vim .env
```

### Create Directories

```bash
# Windows
mkdir data outputs users embeddings

# Mac/Linux
mkdir -p data outputs users embeddings
```

---

## Database/User Management

### Clear User Data

```bash
# Delete users file (Windows)
del users\users.json

# Delete users file (Mac/Linux)
rm users/users.json
```

### Clear Document History

```bash
# Remove all user documents (Windows)
del users\*_docs.json

# Remove all user documents (Mac/Linux)
rm users/*_docs.json
```

### Clear Uploaded Documents

```bash
# Windows
del data\*

# Mac/Linux
rm data/*
```

---

## Development Commands

### Run with Debug Mode

```bash
# Backend with debug
python -m uvicorn backend.api:app --reload --log-level debug

# Frontend with debug
streamlit run app/main.py --logger.level=debug
```

### Access Interactive Python Shell

```bash
# Start Python REPL
python

# Import module
from utils.document_processor import DocumentProcessor

# Exit
exit()
```

### Check Python Path

```bash
# Windows
where python

# Mac/Linux
which python
```

### Check Installed Python

```bash
python --version
python3 --version
```

---

## Environment Variables

### View .env File

```bash
# Windows
type .env

# Mac/Linux
cat .env
```

### Set Temporary Environment Variable

```bash
# Windows Command Prompt
set OPENAI_API_KEY=your-key

# Windows PowerShell
$env:OPENAI_API_KEY='your-key'

# Mac/Linux
export OPENAI_API_KEY='your-key'
```

---

## Useful Links

```
Frontend:        http://localhost:8501
Backend API:     http://localhost:8000
API Docs:        http://localhost:8000/docs
API Redoc:       http://localhost:8000/redoc
Health Check:    http://localhost:8000/health
```

---

## Quick Troubleshooting

### "Module not found"
```bash
# Activate venv
# Windows: .\venv\Scripts\activate.bat
# Mac/Linux: source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### "Port already in use"
```bash
# Find process
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000

# Kill process
# Windows: taskkill /PID <PID> /F
# Mac/Linux: kill -9 <PID>
```

### "Permission denied"
```bash
# Windows - Change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "Python not found"
```bash
# Reinstall Python from https://www.python.org
# Make sure to add to PATH during installation
```

---

## File Locations

```
Project Root:           doc_intelligence_platform/
Frontend Code:          app/main.py
Backend Code:           backend/api.py
Document Processor:     utils/document_processor.py
AI Generator:           utils/ai_generator.py
User Manager:           utils/user_manager.py
Authentication:         utils/auth.py
Uploaded Documents:     data/
Generated Outputs:      outputs/
User Data:             users/
Embeddings:            embeddings/
Configuration:         .env
Requirements:          requirements.txt
```

---

## API Endpoints Quick Reference

```
POST   /signup                  - Create new account
POST   /login                   - Login to account
POST   /upload                  - Upload document
POST   /summarize              - Generate summary
POST   /notes                  - Generate notes
POST   /email                  - Generate email
POST   /qa                     - Ask question
GET    /history                - Get user history
GET    /health                 - Health check
```

---

**Save this page for quick reference!**
