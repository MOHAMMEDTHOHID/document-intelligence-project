# 🎯 Complete Installation & Setup Instructions

Follow these exact steps to get the AI Document Intelligence Platform running.

---

## 📋 STEP-BY-STEP GUIDE

### ✅ STEP 1: Verify Python Installation

Open Command Prompt / Terminal and run:

```bash
python --version
```

**Expected output:** `Python 3.8.0` or higher

If you don't have Python:
- Download from: https://www.python.org/downloads/
- During installation, CHECK "Add Python to PATH"
- Restart your computer after installation

---

### ✅ STEP 2: Navigate to Project Folder

**Windows (Command Prompt):**
```cmd
cd C:\Users\YOUR_USERNAME\OneDrive\Documents\folder\doc_intelligence_platform
```

**Mac/Linux:**
```bash
cd ~/Documents/folder/doc_intelligence_platform
```

---

### ✅ STEP 3: Create Virtual Environment

Creating a virtual environment isolates project dependencies.

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

**✓ You should see `(venv)` at the start of your command line**

---

### ✅ STEP 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

This ensures you have the latest package installer.

---

### ✅ STEP 5: Install All Requirements

```bash
pip install -r requirements.txt
```

⏳ **This takes 2-5 minutes. Wait for completion.**

**Success message:** "Successfully installed [packages]"

If you get errors:
```bash
# Try installing specific packages
pip install fastapi
pip install streamlit
pip install uvicorn
pip install PyPDF2
pip install python-docx
pip install openai
```

---

### ✅ STEP 6: Create Configuration File

**Windows:**
```cmd
copy .env.example .env
```

**Mac/Linux:**
```bash
cp .env.example .env
```

Then edit `.env` file:

**Windows (Notepad):**
```cmd
notepad .env
```

**Mac (TextEdit):**
```bash
nano .env
```

**Linux (vim or nano):**
```bash
nano .env
```

Edit and update:
```
OPENAI_API_KEY=sk-your-actual-key-here
SECRET_KEY=change-this-to-random-string
```

Save and close the file.

---

### ✅ STEP 7: Test Installation

Verify everything is set up correctly:

```bash
python test_installation.py
```

**Expected output:**
```
✓ Python version OK
✓ FastAPI
✓ Streamlit
✓ Pydantic
✓ PyPDF2
✓ All tests passed!
```

If any test fails, check the error message and reinstall that package.

---

### ✅ STEP 8: Create Necessary Directories

**Windows:**
```cmd
mkdir data outputs users embeddings
```

**Mac/Linux:**
```bash
mkdir -p data outputs users embeddings
```

---

## 🚀 RUNNING THE APPLICATION

### Method 1: Simple Menu (Recommended for First Time)

```bash
python main.py
```

You'll see:
```
1. Install requirements
2. Start Backend API only
3. Start Frontend only
4. Start both Backend & Frontend  ← Select THIS
5. Run tests
6. Exit
```

**Type:** `4` and press Enter

Wait for messages:
```
✓ Backend started!
✓ Frontend started!
```

Then browser opens automatically.

---

### Method 2: Manual (Advanced)

If Method 1 doesn't work, open TWO separate terminals/command prompts:

**Terminal 1 - Backend:**
```bash
python -m uvicorn backend.api:app --reload
```

Wait for:
```
Uvicorn running on http://0.0.0.0:8000
Application startup complete
```

**Terminal 2 - Frontend:**
```bash
streamlit run app/main.py
```

Wait for:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

---

## ✅ VERIFY APPLICATION IS RUNNING

### Check in Your Browser

1. **Frontend**: http://localhost:8501
   - Should show login page
   
2. **Backend API**: http://localhost:8000
   - Should show JSON response
   
3. **API Documentation**: http://localhost:8000/docs
   - Should show interactive API documentation

---

## 🧪 TEST THE APPLICATION

### Create Test Account

1. Go to: http://localhost:8501
2. Click "Sign Up"
3. Enter:
   - **Email:** test@example.com
   - **Password:** test123456
4. Click "Sign Up"
5. Click "Login"
6. Enter credentials and login

### Test Upload Feature

1. After login, click "Upload Document"
2. Click "Choose a document"
3. Select any text file (or create one with sample text)
4. Click "Process Document"
5. You should see character count

### Test Summary Generation

1. Go to "Summarize" tab
2. Click "Generate Summary"
3. You should see a summary
4. Click "Download Summary"

### Test Q&A Feature

1. Go to "Q&A" tab
2. Ask a question like: "What is the main topic?"
3. Click "Get Answer"
4. You should see an answer based on document

---

## 📁 FILE STRUCTURE AFTER SETUP

Your project should look like:
```
doc_intelligence_platform/
├── main.py                    ← Run this
├── requirements.txt
├── test_installation.py
├── .env                       ← Your configuration
├── README.md                  ← Full documentation
├── QUICKSTART.md
├── SETUP_GUIDE.md
├── FILES_OVERVIEW.md
│
├── app/
│   ├── __init__.py
│   └── main.py               ← Frontend UI
│
├── backend/
│   ├── __init__.py
│   └── api.py                ← Backend API
│
├── utils/
│   ├── __init__.py
│   ├── auth.py
│   ├── ai_generator.py
│   ├── document_processor.py
│   └── user_manager.py
│
├── data/                      ← Upload documents here
├── outputs/                   ← Generated files here
├── users/                     ← User data stored here
└── embeddings/               ← Embeddings stored here
```

---

## 📡 API ENDPOINTS TO TEST

### Using Browser

1. **Health Check:** http://localhost:8000/health
2. **API Docs:** http://localhost:8000/docs
3. **Frontend:** http://localhost:8501

### Using Command Line (curl)

```bash
# Test health check
curl http://localhost:8000/health

# Test signup
curl -X POST http://localhost:8000/signup ^
  -H "Content-Type: application/json" ^
  -d "{\"email\":\"test2@example.com\",\"password\":\"test123456\"}"
```

---

## 🛑 STOPPING THE APPLICATION

### Using Menu
- Press Ctrl+C in the terminal showing the menu

### If Running Manually
- Terminal 1 (Backend): Press Ctrl+C
- Terminal 2 (Frontend): Press Ctrl+C or Ctrl+Z

### Closing Completely
```bash
# Kill all Python processes
# Windows (PowerShell):
Get-Process python | Stop-Process -Force

# Mac/Linux:
killall python
```

---

## 🔄 RESTARTING THE APPLICATION

The app restarts quickly after changes:

**For Backend Changes:**
- Files auto-reload with `--reload` flag
- Just refresh API docs page

**For Frontend Changes:**
- Files auto-refresh
- Just refresh browser

**Full Restart:**
- Stop both services (Ctrl+C)
- Run `python main.py` again
- Select option 4

---

## 🆘 TROUBLESHOOTING

### Problem: "Python command not found"

**Solution 1:** Reinstall Python
- Download from https://www.python.org
- **Important:** Check "Add to PATH" during installation

**Solution 2:** Use full path
```bash
# Windows
C:\Python310\python.exe --version

# Mac
/usr/local/bin/python3 --version
```

---

### Problem: "No module named 'fastapi'"

**Solution:**
```bash
# Make sure venv is activated (check for (venv) prefix)
# Windows: .\venv\Scripts\activate.bat
# Mac/Linux: source venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt

# Or install specific package
pip install fastapi
```

---

### Problem: "Port 8000 already in use"

**Solution:**

**Windows:**
```cmd
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

**Mac/Linux:**
```bash
lsof -i :8000
kill -9 <PID>
```

Or use different port:
```bash
python -m uvicorn backend.api:app --reload --port 8001
```

---

### Problem: "Frontend not loading"

**Solution 1:** Try opening manually
```
http://localhost:8501
```

**Solution 2:** Check if backend is running
```
http://localhost:8000/health
```

**Solution 3:** Use different port
```bash
streamlit run app/main.py --server.port 8502
```

---

### Problem: "ModuleNotFoundError after requirements install"

**Solution:**
```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall

# Or clean and reinstall
pip cache purge
pip install -r requirements.txt
```

---

## ⚙️ CONFIGURATION

### Update API Keys

Edit `.env`:

```bash
# Windows
notepad .env

# Mac/Linux
nano .env
```

Update:
```
OPENAI_API_KEY=sk-your-actual-key-from-openai
SECRET_KEY=pick-a-random-secure-string
```

### Change Ports

**Backend on port 8001:**
```bash
python -m uvicorn backend.api:app --reload --port 8001
```

**Frontend on port 8502:**
```bash
streamlit run app/main.py --server.port 8502
```

---

## 📚 NEXT STEPS

After successful setup:

1. **Read Documentation**
   - `README.md` - Full guide
   - `FILES_OVERVIEW.md` - File descriptions
   - `COMMANDS_CHEATSHEET.md` - Quick reference

2. **Explore Features**
   - Upload documents
   - Generate summaries
   - Create notes and emails
   - Ask questions about documents

3. **Integrate with OpenAI (Optional)**
   - Get API key from https://platform.openai.com
   - Add to `.env`
   - Update `utils/ai_generator.py` to use OpenAI

4. **Deploy Application** (Later)
   - See `README.md` for deployment options
   - Consider using Docker
   - Use cloud services (AWS, GCP, Heroku)

---

## ✅ QUICK CHECKLIST

Before running:
- [ ] Python 3.8+ installed
- [ ] In correct project folder
- [ ] Virtual environment created
- [ ] Virtual environment activated (see `(venv)` in terminal)
- [ ] Requirements installed
- [ ] `.env` file created and configured
- [ ] Test passed: `python test_installation.py`

Ready to run:
- [ ] Terminal 1: Backend API
- [ ] Terminal 2: Frontend UI
- [ ] Browser opens automatically
- [ ] Can access http://localhost:8501
- [ ] Can create account
- [ ] Can upload document
- [ ] Can generate summary

---

## 📞 NEED HELP?

1. **Check Troubleshooting** section above
2. **Run test:** `python test_installation.py`
3. **Read error message** carefully
4. **Check logs** in terminal
5. **Verify .env** file is correct
6. **Try restarting** services

---

**🎉 Congratulations! Your Document Intelligence Platform is ready!**

**Next:** Go to http://localhost:8501 and start using the platform!
