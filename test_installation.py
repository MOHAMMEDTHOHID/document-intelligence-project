"""
Test script to verify installation and basic functionality
"""

import sys
import subprocess
from pathlib import Path

def test_python_version():
    """Test Python version"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} OK\n")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Need 3.8+\n")
        return False

def test_imports():
    """Test critical imports"""
    print("Testing imports...")
    imports = [
        ('fastapi', 'FastAPI'),
        ('streamlit', 'Streamlit'),
        ('pydantic', 'Pydantic'),
        ('PyPDF2', 'PyPDF2'),
    ]
    
    all_ok = True
    for module, name in imports:
        try:
            __import__(module)
            print(f"✓ {name}")
        except ImportError:
            print(f"❌ {name} - NOT installed")
            all_ok = False
    
    print()
    return all_ok

def test_directories():
    """Test necessary directories"""
    print("Testing directories...")
    dirs = ['data', 'outputs', 'users', 'embeddings', 'utils', 'app', 'backend']
    
    all_ok = True
    for d in dirs:
        path = Path(d)
        if path.exists():
            print(f"✓ {d}/")
        else:
            print(f"❌ {d}/ - NOT found")
            all_ok = False
    
    print()
    return all_ok

def test_files():
    """Test necessary files"""
    print("Testing files...")
    files = [
        'main.py',
        'requirements.txt',
        'backend/api.py',
        'app/main.py',
        'utils/document_processor.py',
        'utils/ai_generator.py',
        'utils/user_manager.py',
    ]
    
    all_ok = True
    for f in files:
        path = Path(f)
        if path.exists():
            print(f"✓ {f}")
        else:
            print(f"❌ {f} - NOT found")
            all_ok = False
    
    print()
    return all_ok

def test_api_structure():
    """Test API basic structure"""
    print("Testing API structure...")
    try:
        from backend.api import app
        print("✓ FastAPI app imported successfully")
        print()
        return True
    except Exception as e:
        print(f"❌ Error importing API: {e}\n")
        return False

def test_utils_structure():
    """Test utils structure"""
    print("Testing utils structure...")
    try:
        from utils.document_processor import DocumentProcessor
        from utils.ai_generator import AIGenerator
        from utils.user_manager import UserManager
        print("✓ DocumentProcessor")
        print("✓ AIGenerator")
        print("✓ UserManager")
        print()
        return True
    except Exception as e:
        print(f"❌ Error importing utils: {e}\n")
        return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("Document Intelligence Platform - Installation Test")
    print("="*60 + "\n")
    
    results = []
    
    results.append(("Python Version", test_python_version()))
    results.append(("Imports", test_imports()))
    results.append(("Directories", test_directories()))
    results.append(("Files", test_files()))
    results.append(("API Structure", test_api_structure()))
    results.append(("Utils Structure", test_utils_structure()))
    
    # Summary
    print("="*60)
    print("Test Summary")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print("="*60)
    print(f"\nTotal: {passed}/{total} tests passed\n")
    
    if passed == total:
        print("✓ All tests passed! Ready to run.")
        print("\nNext steps:")
        print("1. Update .env with your API keys")
        print("2. Run: python main.py")
        print("3. Select option 4 to start both services\n")
    else:
        print("❌ Some tests failed. Please check the errors above.\n")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
