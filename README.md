# 📄 Document Intelligence Platform

An AI-powered document intelligence platform that processes documents, generates summaries, notes, emails, and enables document-based Q&A.

## 📋 Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)

## ✨ Features

- **Multi-document Support**: Upload PDF, DOCX, and TXT files
- **AI-based Summarization**: Automatic document summarization
- **Email Generation**: Generate professional emails from documents
- **Notes Generation**: Create structured notes from documents
- **Document-based Q&A**: Ask questions about uploaded documents
- **User Authentication**: Secure login and signup system
- **Document History**: Track all uploaded documents
- **Downloadable Outputs**: Export summaries, notes, and emails

## 📁 Project Structure

```
doc_intelligence_platform/
│
├── app/
│   └── main.py                 # Streamlit frontend
│
├── backend/
│   └── api.py                  # FastAPI backend API
│
├── utils/
│   ├── __init__.py
│   ├── document_processor.py   # Document text extraction
│   ├── ai_generator.py         # AI content generation
│   ├── user_manager.py         # User management
│   └── auth.py                 # Authentication & JWT
│
├── prompts/                    # AI prompt templates
├── data/                       # Uploaded documents
├── outputs/                    # Generated outputs
├── users/                      # User data & history
├── embeddings/                 # Document embeddings
│
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
└── README.md                   # This file
```

## 🚀 Setup Instructions

### Step 1: Clone/Download the Project

```bash
cd doc_intelligence_platform
```

### Step 2: Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
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

**If you get errors with faiss-cpu, try:**
```bash
pip install faiss-cpu
```

**Or on Windows:**
```bash
pip install faiss-cpu==1.7.4
```

### Step 4: Setup Environment Variables

```bash
# Create .env file from template
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux
```

Edit `.env` and add:
```
OPENAI_API_KEY=your-actual-api-key
SECRET_KEY=your-secret-key-for-jwt
```

### Step 5: Create Necessary Directories

```bash
mkdir data outputs users embeddings embeddings
```

## 📦 Running the Application

### Option 1: Using the Main Menu Script

```bash
python main.py
```

Then select:
- `1` - Install requirements
- `4` - Start both Backend & Frontend

### Option 2: Manual Setup

**Terminal 1 - Start Backend API:**
```bash
python -m uvicorn backend.api:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start Frontend:**
```bash
streamlit run app/main.py
```

### Option 3: Individual Services

**Backend only:**
```bash
python -m uvicorn backend.api:app --reload
# API runs on: http://localhost:8000
# Docs: http://localhost:8000/docs
```

**Frontend only:**
```bash
streamlit run app/main.py
# Runs on: http://localhost:8501
```

## 🌐 Access the Application

- **Frontend UI**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 📡 API Endpoints

### Authentication

```bash
# Signup
POST /signup
Body: {"email": "user@example.com", "password": "password123"}

# Login
POST /login
Body: {"email": "user@example.com", "password": "password123"}
```

### Document Management

```bash
# Upload Document
POST /upload
Form Data: file (multipart)

# Get History
GET /history?user_id=1
```

### Content Generation

```bash
# Generate Summary
POST /summarize?document_id=doc.pdf&user_id=1

# Generate Notes
POST /notes?document_id=doc.pdf&user_id=1

# Generate Email
POST /email?document_id=doc.pdf&email_type=summary&user_id=1

# Answer Question
POST /qa
Body: {"question": "What is this document about?", "document_id": "doc.pdf"}
```

## 🧪 Testing the API

### Using cURL

```bash
# Test Health Check
curl http://localhost:8000/health

# Signup
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"

# Login
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@example.com\",\"password\":\"password123\"}"
```

### Using Postman

1. Open Postman
2. Import API endpoints
3. Create requests for each endpoint
4. Test with sample data

## 💡 Usage Examples

### Example 1: Upload and Summarize a Document

1. Start both services
2. Go to http://localhost:8501
3. Sign up or login
4. Click "Upload Document"
5. Select a PDF/DOCX/TXT file
6. Click "Process Document"
7. Go to "Summarize" tab
8. Click "Generate Summary"
9. Download the summary

### Example 2: Ask Questions About a Document

1. Upload a document (see Example 1)
2. Go to "Q&A" tab
3. Type your question
4. Click "Get Answer"
5. View the answer

### Example 3: Generate Professional Email

1. Upload a document
2. Go to "Generate Email"
3. Select email type (Summary/Follow-up/Action Items)
4. Click "Generate Email"
5. Copy or download the email

## 🔧 Troubleshooting

### Port Already in Use

```bash
# Find and kill process on port 8000 (Backend)
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8000
kill -9 <PID>

# For Port 8501 (Frontend)
# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### ModuleNotFoundError

```bash
# Verify venv is activated
which python  # Mac/Linux
where python  # Windows

# Should show path inside venv/
# If not, activate venv again
```

### Requirements Installation Issues

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt -v
```

### File Upload Errors

- Ensure `data/` directory exists
- Check file permissions
- Verify file format (PDF, DOCX, TXT)

## 🔐 Security Notes

⚠️ **Important for Production:**

1. Change `SECRET_KEY` in `.env`
2. Use environment variables for API keys
3. Enable HTTPS
4. Use database instead of JSON files
5. Implement rate limiting
6. Add input validation
7. Use proper password hashing (already implemented)

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| fastapi | 0.104.1 | Backend API framework |
| streamlit | 1.28.1 | Frontend UI framework |
| uvicorn | 0.24.0 | ASGI server |
| PyPDF2 | 3.0.1 | PDF processing |
| python-docx | 0.8.11 | DOCX processing |
| faiss-cpu | 1.7.4 | Vector search |
| openai | 1.3.5 | OpenAI API client |

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

## 📝 License

This project is open source and available under the MIT License.

## 🎯 Future Enhancements

- [ ] Integration with OpenAI/Claude APIs
- [ ] Document embedding with FAISS
- [ ] Advanced NLP features
- [ ] Multi-language support
- [ ] Batch processing
- [ ] Database integration (PostgreSQL)
- [ ] Advanced user management
- [ ] File versioning
- [ ] Collaboration features

## 📧 Support

For issues and questions, please refer to the troubleshooting section above.

---

**Created with ❤️ for Document Intelligence**
