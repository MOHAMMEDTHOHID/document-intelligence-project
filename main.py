#!/usr/bin/env python3
"""
Document Intelligence Platform - Main Entry Point
This script helps manage the application (backend and frontend)
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    print("\n" + "="*60)
    print("📄 Document Intelligence Platform")
    print("="*60 + "\n")

def check_requirements():
    """Check if requirements are installed"""
    print("✓ Checking requirements...")
    requirements_file = "requirements.txt"
    
    if not os.path.exists(requirements_file):
        print("❌ requirements.txt not found!")
        return False
    
    print("✓ requirements.txt found\n")
    return True

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing requirements...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✓ Requirements installed successfully!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}\n")
        return False

def start_backend():
    """Start FastAPI backend"""
    print("\n🚀 Starting Backend API...")
    print("   - API will run on: http://localhost:8000")
    print("   - Docs: http://localhost:8000/docs\n")
    
    try:
        subprocess.Popen([
            sys.executable, "-m", "uvicorn",
            "backend.api:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000"
        ])
        time.sleep(3)
        print("✓ Backend started!\n")
        return True
    except Exception as e:
        print(f"❌ Error starting backend: {e}\n")
        return False

def start_frontend():
    """Start Streamlit frontend"""
    print("\n💻 Starting Frontend...")
    print("   - Frontend will run on: http://localhost:8501\n")
    
    try:
        subprocess.Popen([
            sys.executable, "-m", "streamlit", "run",
            "app/main.py"
        ])
        print("✓ Frontend started!\n")
        return True
    except Exception as e:
        print(f"❌ Error starting frontend: {e}\n")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    
    if not os.path.exists(env_file):
        print("\n📝 Creating .env file...")
        env_content = """# OpenAI API Configuration
OPENAI_API_KEY=your-api-key-here

# JWT Secret
SECRET_KEY=your-secret-key-change-in-production

# Database
DATABASE_URL=sqlite:///./docs_intelligence.db

# Environment
DEBUG=True
"""
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✓ .env file created. Please update it with your API keys!\n")
    else:
        print("✓ .env file already exists\n")

def show_menu():
    """Show main menu"""
    print("\n" + "="*60)
    print("Select an option:")
    print("="*60)
    print("1. Install requirements")
    print("2. Start Backend API only")
    print("3. Start Frontend only")
    print("4. Start both Backend & Frontend")
    print("5. Run tests")
    print("6. Exit")
    print("="*60 + "\n")

def main():
    """Main function"""
    print_banner()
    
    # Create necessary directories
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("users", exist_ok=True)
    os.makedirs("embeddings", exist_ok=True)
    
    # Create .env file
    create_env_file()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            install_requirements()
        
        elif choice == "2":
            start_backend()
            input("\nPress Enter to return to menu...")
        
        elif choice == "3":
            start_frontend()
            input("\nPress Enter to return to menu...")
        
        elif choice == "4":
            start_backend()
            time.sleep(2)
            start_frontend()
            print("\n✓ Both services started!")
            print("\nAccess the application:")
            print("   - Frontend: http://localhost:8501")
            print("   - Backend: http://localhost:8000")
            print("   - API Docs: http://localhost:8000/docs\n")
            input("Press Enter to return to menu...")
        
        elif choice == "5":
            print("\n🧪 Running tests...")
            print("Note: Test file needs to be created\n")
        
        elif choice == "6":
            print("\n👋 Goodbye!\n")
            sys.exit(0)
        
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
