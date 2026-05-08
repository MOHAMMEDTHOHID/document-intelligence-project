from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
from datetime import datetime
from utils.document_processor import DocumentProcessor
from utils.ai_generator import AIGenerator
from utils.user_manager import UserManager
from utils.auth import create_access_token, verify_token

app = FastAPI(title="Document Intelligence API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class UserLogin(BaseModel):
    email: str
    password: str

class UserSignup(BaseModel):
    email: str
    password: str

class Document(BaseModel):
    filename: str
    content: str
    summary: str = None
    notes: str = None

class Question(BaseModel):
    question: str
    document_id: str

# Initialize components
user_manager = UserManager()
doc_processor = DocumentProcessor()
ai_generator = AIGenerator()

# Routes
@app.get("/")
async def root():
    return {"message": "Document Intelligence Platform API"}

@app.post("/signup")
async def signup(user: UserSignup):
    """User signup"""
    try:
        result = user_manager.create_user(user.email, user.password)
        if result:
            return {"message": "User created successfully", "email": user.email}
        else:
            raise HTTPException(status_code=400, detail="User already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
async def login(user: UserLogin):
    """User login"""
    try:
        user_data = user_manager.authenticate_user(user.email, user.password)
        if user_data:
            token = create_access_token(data={"sub": user.email})
            return {
                "id": user_data["id"],
                "email": user.email,
                "token": token,
                "message": "Login successful"
            }
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_document(file: UploadFile = File(...), user_id: str = ""):
    """Upload and process document"""
    try:
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", file.filename)
        
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Extract text
        text = doc_processor.extract_text(file_path)
        
        # Store metadata
        metadata = {
            "filename": file.filename,
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
            "path": file_path,
            "char_count": len(text)
        }
        
        # Save metadata
        os.makedirs("users", exist_ok=True)
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        docs_list = []
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as f:
                docs_list = json.load(f)
        docs_list.append(metadata)
        with open(metadata_path, "w") as f:
            json.dump(docs_list, f)
        
        return {
            "message": "Document uploaded successfully",
            "filename": file.filename,
            "char_count": len(text)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize_document(document_id: str, user_id: str = ""):
    """Generate summary"""
    try:
        # Get document content
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        with open(metadata_path, "r") as f:
            docs = json.load(f)
        
        doc = next((d for d in docs if d["filename"] == document_id), None)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        # Read content
        with open(doc["path"], "r", encoding="utf-8") as f:
            content = f.read()
        
        # Generate summary
        summary = ai_generator.generate_summary(content)
        
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/notes")
async def generate_notes(document_id: str, user_id: str = ""):
    """Generate notes"""
    try:
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        with open(metadata_path, "r") as f:
            docs = json.load(f)
        
        doc = next((d for d in docs if d["filename"] == document_id), None)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        with open(doc["path"], "r", encoding="utf-8") as f:
            content = f.read()
        
        notes = ai_generator.generate_notes(content)
        
        return {"notes": notes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/email")
async def generate_email(document_id: str, email_type: str = "summary", user_id: str = ""):
    """Generate email"""
    try:
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        with open(metadata_path, "r") as f:
            docs = json.load(f)
        
        doc = next((d for d in docs if d["filename"] == document_id), None)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        with open(doc["path"], "r", encoding="utf-8") as f:
            content = f.read()
        
        email = ai_generator.generate_email(content, email_type)
        
        return {"email": email}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/qa")
async def answer_question(question: Question, user_id: str = ""):
    """Answer question about document"""
    try:
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        with open(metadata_path, "r") as f:
            docs = json.load(f)
        
        doc = next((d for d in docs if d["filename"] == question.document_id), None)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        
        with open(doc["path"], "r", encoding="utf-8") as f:
            content = f.read()
        
        answer = ai_generator.answer_question(content, question.question)
        
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history(user_id: str = ""):
    """Get user document history"""
    try:
        metadata_path = os.path.join("users", f"{user_id}_docs.json")
        if not os.path.exists(metadata_path):
            return []
        
        with open(metadata_path, "r") as f:
            docs = json.load(f)
        
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
