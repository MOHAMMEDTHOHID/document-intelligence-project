# 🏃 RUN NOW - Copy & Paste Commands

This file contains all commands you need. Just copy and paste!

---

## WINDOWS USERS - COPY & PASTE THESE COMMANDS

### Step 1: Create Virtual Environment
```
python -m venv venv
.\venv\Scripts\activate.ps1
```

### Step 2: Install Requirements
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Create Configuration
```
copy .env.example .env
```
Then edit `.env` with notepad and add your API keys.

### Step 4: Test Installation
```
python test_installation.py
```

### Step 5: Run Application
```
python main.py
```
Select option `4` when menu appears.

---

## MAC/LINUX USERS - COPY & PASTE THESE COMMANDS

### Step 1: Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Requirements
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Create Configuration
```
cp .env.example .env
nano .env
```
Edit and save (Ctrl+X then Y in nano).

### Step 4: Test Installation
```
python3 test_installation.py
```

### Step 5: Run Application
```
python3 main.py
```
Select option `4` when menu appears.

---

## QUICK REFERENCE - ALL COMMANDS

### Activate Virtual Environment (Each Time)

**Windows:**
```
.\venv\Scripts\activate.ps1
```

**Mac/Linux:**
```
source venv/bin/activate
```

### Start Services

**Option A - Simple (Recommended):**
```
python main.py
```
Then select option 4

**Option B - Backend Only:**
```
python -m uvicorn backend.api:app --reload
```

**Option C - Frontend Only:**
```
streamlit run app/main.py
```

**Option D - Both Manual (2 Terminals):**

Terminal 1:
```
python -m uvicorn backend.api:app --reload
```

Terminal 2:
```
streamlit run app/main.py
```

### Test Application

```bash
# Test health check
curl http://localhost:8000/health

# Test signup
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

### Troubleshooting

**Fix port already in use (Windows):**
```
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

**Fix module not found:**
```
pip install -r requirements.txt
```

**Fix venv not working:**
```
# Windows:
python -m venv venv
.\venv\Scripts\activate.ps1

# Mac/Linux:
python3 -m venv venv
source venv/bin/activate
```

---

## 🎯 FASTEST PATH TO RUNNING

### For Windows (PowerShell)

Copy and run these one by one:

```powershell
# 1. Navigate to folder (adjust path as needed)
cd "C:\Users\YOUR_NAME\OneDrive\Documents\folder\doc_intelligence_platform"

# 2. Create environment
python -m venv venv

# 3. Activate
.\venv\Scripts\Activate.ps1

# 4. Install packages
python -m pip install --upgrade pip
pip install -r requirements.txt

# 5. Create config
copy .env.example .env

# Edit .env file (open with notepad)
notepad .env

# 6. Test
python test_installation.py

# 7. Run!
python main.py
```

Then select option `4` in menu.

### For Mac/Linux

Copy and run these one by one:

```bash
# 1. Navigate to folder (adjust path as needed)
cd ~/Documents/folder/doc_intelligence_platform

# 2. Create environment
python3 -m venv venv

# 3. Activate
source venv/bin/activate

# 4. Install packages
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# 5. Create config
cp .env.example .env

# Edit .env file
nano .env

# 6. Test
python3 test_installation.py

# 7. Run!
python3 main.py
```

Then select option `4` in menu.

---

## ✅ AFTER RUNNING

### Access Points

- **Frontend:** http://localhost:8501
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

### First Login

1. Click "Sign Up"
2. Email: `test@example.com`
3. Password: `test123456`
4. Click "Sign Up"
5. Login with same credentials

### Test Features

1. Upload a document
2. Click "Summarize"
3. Click "Generate Summary"
4. See the result!

---

## 🆘 IF SOMETHING GOES WRONG

### "python: command not found"
```bash
# Reinstall Python from https://www.python.org
# Make sure to ADD TO PATH during installation
# Then restart your computer
```

### "ModuleNotFoundError"
```bash
# Activate venv first (see above)
# Then run:
pip install -r requirements.txt
```

### "Port 8000 already in use"
```bash
# Windows:
netstat -ano | findstr :8000
taskkill /PID <number> /F

# Mac/Linux:
lsof -i :8000
kill -9 <PID>
```

### "Can't activate venv"
```bash
# Windows - Allow scripts:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then:
.\venv\Scripts\Activate.ps1
```

---

## 📞 NEED MORE HELP?

1. Read: **COMPLETE_SETUP.md** for detailed guide
2. Read: **README.md** for full documentation
3. Check: **COMMANDS_CHEATSHEET.md** for all commands
4. Run: `python test_installation.py` to verify setup

---

## 🎯 COPY-PASTE CHECKLIST

Check these off as you complete:

- [ ] Opened terminal/command prompt
- [ ] Navigated to project folder
- [ ] Ran: `python -m venv venv`
- [ ] Activated virtual environment
- [ ] Ran: `pip install -r requirements.txt`
- [ ] Ran: `copy .env.example .env` (Windows) or `cp .env.example .env` (Mac/Linux)
- [ ] Edited `.env` file with API keys
- [ ] Ran: `python test_installation.py` - All tests passed ✓
- [ ] Ran: `python main.py`
- [ ] Selected option `4`
- [ ] Opened browser to http://localhost:8501
- [ ] Created account
- [ ] Uploaded document
- [ ] Generated summary

---

**THAT'S IT! You're done! 🎉**

Now go to http://localhost:8501 and start using the platform!
