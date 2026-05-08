# 📁 Project Files Overview

Complete description of all files and their purposes.

## Root Files

### `main.py`
- **Purpose**: Application entry point with interactive menu
- **Used for**: Starting backend, frontend, or both
- **Run**: `python main.py`

### `requirements.txt`
- **Purpose**: Lists all Python package dependencies
- **Used for**: Installing packages with `pip install -r requirements.txt`
- **Key packages**: fastapi, streamlit, PyPDF2, python-docx, openai, faiss, etc.

### `.env.example`
- **Purpose**: Template for environment variables
- **Used for**: Creating your own `.env` file
- **Action**: Copy to `.env` and fill in your values

### `.env` (create from template)
- **Purpose**: Stores sensitive configuration
- **Includes**: API keys, secret keys, database URLs
- **Important**: Never commit to git!

### `test_installation.py`
- **Purpose**: Verify installation is complete
- **Run**: `python test_installation.py`
- **Checks**: Python version, imports, directories, files

---

## Documentation Files

### `README.md`
- **Purpose**: Main project documentation
- **Contents**: 
  - Feature overview
  - Project structure
  - Setup instructions
  - API endpoints
  - Troubleshooting

### `QUICKSTART.md`
- **Purpose**: Get running in 5 minutes
- **Contents**:
  - Fast setup steps
  - Quick commands
  - Common issues

### `SETUP_GUIDE.md`
- **Purpose**: Detailed step-by-step setup
- **Contents**:
  - Windows/Mac/Linux specific steps
  - Verification procedures
  - Troubleshooting

### `COMMANDS_CHEATSHEET.md`
- **Purpose**: Quick command reference
- **Contents**:
  - All important commands
  - File locations
  - API endpoints

---

## App Directory (`app/`)

### `app/__init__.py`
- **Purpose**: Makes app a Python package
- **Content**: Empty initialization file

### `app/main.py`
- **Purpose**: Streamlit frontend UI
- **Features**:
  - User login/signup
  - Document upload
  - Summary generation
  - Notes generation
  - Email generation
  - Document Q&A
  - User history
- **Run**: `streamlit run app/main.py`

---

## Backend Directory (`backend/`)

### `backend/__init__.py`
- **Purpose**: Makes backend a Python package
- **Content**: Empty initialization file

### `backend/api.py`
- **Purpose**: FastAPI backend server
- **Features**:
  - User authentication (signup/login)
  - Document upload and processing
  - Content generation endpoints
  - Q&A endpoint
  - User history tracking
- **Run**: `python -m uvicorn backend.api:app --reload`
- **Docs**: http://localhost:8000/docs

---

## Utils Directory (`utils/`)

### `utils/__init__.py`
- **Purpose**: Makes utils a Python package
- **Content**: Empty initialization file

### `utils/document_processor.py`
- **Purpose**: Extract text from documents
- **Functions**:
  - `extract_text()` - Extract from any format
  - `_extract_pdf()` - PDF extraction
  - `_extract_docx()` - Word document extraction
  - `_extract_txt()` - Text file extraction
  - `chunk_text()` - Split text into chunks
  - `clean_text()` - Normalize text
- **Formats**: PDF, DOCX, TXT

### `utils/ai_generator.py`
- **Purpose**: Generate AI-powered content
- **Functions**:
  - `generate_summary()` - Create document summary
  - `generate_notes()` - Generate structured notes
  - `generate_email()` - Create professional emails
  - `answer_question()` - Answer questions about document
  - `extract_keywords()` - Extract important keywords
  - `_score_sentence()` - Score sentence importance
- **Note**: Demo version uses algorithms, production should use OpenAI API

### `utils/user_manager.py`
- **Purpose**: Manage user accounts
- **Functions**:
  - `create_user()` - Register new user
  - `authenticate_user()` - Login verification
  - `get_user()` - Retrieve user info
  - `update_user()` - Modify user data
  - `add_document()` - Add to user history
  - `get_user_documents()` - Get all user documents
  - `delete_user()` - Remove user account
- **Storage**: JSON files in `users/` directory

### `utils/auth.py`
- **Purpose**: JWT token authentication
- **Functions**:
  - `create_access_token()` - Generate JWT token
  - `verify_token()` - Validate JWT token
- **Algorithm**: HS256

---

## Data Directories

### `data/`
- **Purpose**: Store uploaded documents
- **Content**: PDF, DOCX, TXT files
- **Auto-created**: Yes (if doesn't exist)

### `outputs/`
- **Purpose**: Store generated content
- **Content**: Summaries, notes, emails
- **Auto-created**: Yes (if doesn't exist)

### `users/`
- **Purpose**: Store user data
- **Content**: 
  - `users.json` - All user accounts
  - `{user_id}_docs.json` - Each user's document history
- **Auto-created**: Yes (if doesn't exist)

### `embeddings/`
- **Purpose**: Store document embeddings
- **Content**: Vector representations (FAISS indices)
- **Note**: For future use with vector search
- **Auto-created**: Yes (if doesn't exist)

### `prompts/`
- **Purpose**: Store AI prompt templates
- **Content**: Prompt engineering templates
- **Note**: Can be extended with custom prompts

---

## Key Features by File

### Authentication Flow
- **File**: `utils/auth.py`, `utils/user_manager.py`
- **Route**: `/signup`, `/login` in `backend/api.py`

### Document Upload
- **File**: `utils/document_processor.py`
- **Route**: `/upload` in `backend/api.py`

### Content Generation
- **File**: `utils/ai_generator.py`
- **Routes**: `/summarize`, `/notes`, `/email`, `/qa`

### User Interface
- **File**: `app/main.py`
- **Framework**: Streamlit

### API Server
- **File**: `backend/api.py`
- **Framework**: FastAPI

---

## File Dependencies

```
main.py
  ├── backend/api.py
  ├── app/main.py
  └── utils/
      ├── document_processor.py
      ├── ai_generator.py
      ├── user_manager.py
      └── auth.py

requirements.txt
  ├── fastapi
  ├── streamlit
  ├── uvicorn
  ├── PyPDF2
  ├── python-docx
  ├── openai
  ├── faiss-cpu
  └── [20+ other packages]

.env
  ├── OPENAI_API_KEY (for API calls)
  ├── SECRET_KEY (for JWT)
  └── [other config]
```

---

## Size and Performance

| File | Size | Purpose |
|------|------|---------|
| `backend/api.py` | ~4KB | API endpoints |
| `app/main.py` | ~7KB | Frontend UI |
| `utils/document_processor.py` | ~2KB | Document handling |
| `utils/ai_generator.py` | ~3KB | Content generation |
| `utils/user_manager.py` | ~3KB | User management |
| `requirements.txt` | ~1KB | Dependencies |

---

## Development Tips

### Adding New Feature
1. Create new function in appropriate `utils/` file
2. Add API endpoint in `backend/api.py`
3. Add UI component in `app/main.py`
4. Update documentation

### Adding New Utility
1. Create new file in `utils/`
2. Add to imports in relevant files
3. Test with `test_installation.py`

### Debugging
- Check logs in terminal
- Use `--log-level debug` flag
- Check `.env` configuration
- Run `test_installation.py`

### Performance
- Document text is cached in session
- Summaries are generated on demand
- User data stored in JSON (upgrade to database for production)

---

## Next Steps

1. **Review Files**: Check each file's content
2. **Understand Flow**: How data flows through system
3. **Configure .env**: Add your API keys
4. **Run Tests**: Execute `test_installation.py`
5. **Start Application**: Run `python main.py`
6. **Explore Features**: Try each function
7. **Extend**: Add new capabilities

---

## File Checklist

```
✓ main.py
✓ requirements.txt
✓ .env.example
✓ test_installation.py
✓ README.md
✓ QUICKSTART.md
✓ SETUP_GUIDE.md
✓ COMMANDS_CHEATSHEET.md
✓ app/main.py
✓ backend/api.py
✓ utils/document_processor.py
✓ utils/ai_generator.py
✓ utils/user_manager.py
✓ utils/auth.py
✓ data/ (directory)
✓ outputs/ (directory)
✓ users/ (directory)
✓ embeddings/ (directory)
```

---

**All files are now in place. Ready to run!**
