"""
Configuration file for Document Intelligence Platform
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# Frontend Configuration
FRONTEND_PORT = int(os.getenv("FRONTEND_PORT", 8501))

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./docs_intelligence.db")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 2000))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

# File Upload
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 52428800))  # 50MB
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS", "pdf,docx,txt").split(",")

# Application
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Feature Flags
ENABLE_EMAIL_GENERATION = os.getenv("ENABLE_EMAIL_GENERATION", "True").lower() == "true"
ENABLE_QA_FEATURE = os.getenv("ENABLE_QA_FEATURE", "True").lower() == "true"
ENABLE_EMBEDDINGS = os.getenv("ENABLE_EMBEDDINGS", "False").lower() == "true"

# Directories
DATA_DIR = "data"
OUTPUT_DIR = "outputs"
USERS_DIR = "users"
EMBEDDINGS_DIR = "embeddings"
PROMPTS_DIR = "prompts"

# Create directories if they don't exist
for directory in [DATA_DIR, OUTPUT_DIR, USERS_DIR, EMBEDDINGS_DIR, PROMPTS_DIR]:
    os.makedirs(directory, exist_ok=True)

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# API Configuration
API_TITLE = "Document Intelligence Platform API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "AI-powered document intelligence platform"

# CORS Configuration
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8501",
    "http://localhost:8000",
    "*"
]

# Document Processing
MIN_CHUNK_SIZE = 500
MAX_CHUNK_SIZE = 2000
CHUNK_OVERLAP = 100

# Summary Configuration
DEFAULT_SUMMARY_LENGTH = 300
MIN_SUMMARY_LENGTH = 100
MAX_SUMMARY_LENGTH = 1000

# Email Templates
EMAIL_SIGNATURE = "Best regards,\nDocument Intelligence Platform"

# Rate Limiting (for future use)
RATE_LIMIT_ENABLED = False
RATE_LIMIT_REQUESTS = 100
RATE_LIMIT_WINDOW = 3600  # 1 hour

def print_config():
    """Print current configuration (for debugging)"""
    print("\n" + "="*60)
    print("Document Intelligence Platform - Configuration")
    print("="*60)
    print(f"Environment: {ENVIRONMENT}")
    print(f"Debug Mode: {DEBUG}")
    print(f"API: {API_HOST}:{API_PORT}")
    print(f"Frontend Port: {FRONTEND_PORT}")
    print(f"OpenAI API Key: {'Set' if OPENAI_API_KEY else 'Not Set'}")
    print(f"Database: {DATABASE_URL}")
    print(f"Features:")
    print(f"  - Email Generation: {ENABLE_EMAIL_GENERATION}")
    print(f"  - Q&A: {ENABLE_QA_FEATURE}")
    print(f"  - Embeddings: {ENABLE_EMBEDDINGS}")
    print("="*60 + "\n")

if __name__ == "__main__":
    print_config()
