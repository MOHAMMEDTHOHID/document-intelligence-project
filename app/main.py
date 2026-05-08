import streamlit as st
import os
import json
from datetime import datetime
from utils.document_processor import DocumentProcessor
from utils.ai_generator import AIGenerator
from utils.user_manager import UserManager
import requests

# Page configuration
st.set_page_config(page_title="Document Intelligence", layout="wide")

# API endpoint
API_URL = "http://localhost:8000"

# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None
if "documents" not in st.session_state:
    st.session_state.documents = []
if "current_doc" not in st.session_state:
    st.session_state.current_doc = None
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

# Load custom CSS
st.markdown("""
<style>
    .main-title { color: #1f77b4; font-size: 2.5em; margin-bottom: 1em; }
    .section-title { color: #2ca02c; font-size: 1.8em; margin-top: 1.5em; }
    .info-box { background-color: #f0f2f6; padding: 1em; border-radius: 0.5em; }
</style>
""", unsafe_allow_html=True)

def login_page():
    """Login page"""
    st.markdown('<h1 class="main-title">🔐 Document Intelligence Platform</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #666;">📚 Intelligent Document Analysis with AI</h3>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Show Login or Signup based on session state
    if not st.session_state.show_signup:
        # LOGIN PAGE
        st.markdown("### 🔑 Login to Your Account")
        st.info("📌 Enter your credentials to access your documents and AI features")
        
        st.markdown("")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            email = st.text_input("Email", key="login_email", placeholder="your@email.com")
            password = st.text_input("Password", type="password", key="login_password", placeholder="••••••••")
            
            st.markdown("")
            
            if st.button("🚀 Login", use_container_width=True):
                if not email or not password:
                    st.error("❌ Please enter email and password")
                else:
                    try:
                        response = requests.post(f"{API_URL}/login", json={"email": email, "password": password})
                        if response.status_code == 200:
                            st.session_state.user = response.json()
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Invalid credentials")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
            
            st.markdown("---")
            
            if st.button("📝 Create New Account", use_container_width=True):
                st.session_state.show_signup = True
                st.rerun()
    
    else:
        # SIGNUP PAGE
        st.markdown("### 📝 Create New Account")
        st.info("✨ Sign up to start using Document Intelligence Platform")
        
        st.markdown("")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            new_email = st.text_input("Email", key="signup_email", placeholder="your@email.com")
            new_password = st.text_input("Password", type="password", key="signup_password", placeholder="••••••••")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password", placeholder="••••••••")
            
            st.markdown("")
            
            if st.button("✍️ Create Account", use_container_width=True):
                if not new_email or not new_password:
                    st.error("❌ Please fill in all fields")
                elif new_password != confirm_password:
                    st.error("❌ Passwords don't match!")
                elif len(new_password) < 6:
                    st.error("❌ Password must be at least 6 characters")
                else:
                    try:
                        response = requests.post(f"{API_URL}/signup", json={"email": new_email, "password": new_password})
                        if response.status_code == 200:
                            st.success("✅ Signup successful! Redirecting to login...")
                            st.session_state.show_signup = False
                            st.rerun()
                        else:
                            st.error("❌ Signup failed - Email might already exist")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
            
            st.markdown("---")
            
            if st.button("🔙 Back to Login", use_container_width=True):
                st.session_state.show_signup = False
                st.rerun()

def main_app():
    """Main application page"""
    st.markdown('<h1 class="main-title">📄 Document Intelligence Platform</h1>', unsafe_allow_html=True)
    
    # Check if user is logged in
    if st.session_state.user is None:
        st.error("❌ You must be logged in to access this page!")
        st.stop()
    
    # Display user info
    st.success(f"✅ Logged in as: {st.session_state.user['email']}")
    
    # Sidebar
    with st.sidebar:
        st.subheader(f"👤 {st.session_state.user['email']}")
        if st.button("🚪 Logout"):
            st.session_state.user = None
            st.session_state.show_signup = False
            st.rerun()
        
        st.markdown("---")
        
        # Show upload status
        if st.session_state.current_doc:
            st.success(f"📄 Loaded: {st.session_state.current_doc['name']}")
        else:
            st.warning("⚠️ No document loaded")
        
        st.markdown("---")
        st.subheader("Features")
        feature = st.radio("Select Feature", 
            ["📤 Upload Document", "📝 Summarize", "📋 Generate Notes", "❓ Q&A", "📚 History"])
    
    # Main content
    if feature == "📤 Upload Document":
        st.markdown('<h2 class="section-title">📤 Upload Document</h2>', unsafe_allow_html=True)
        st.info("✨ Upload a document (PDF, DOCX, or TXT) to get started with AI features")
        
        uploaded_file = st.file_uploader("Choose a document", type=["pdf", "docx", "txt"], key="doc_uploader")
        if uploaded_file:
            st.info(f"📎 File: {uploaded_file.name}")
            if st.button("✅ Process Document"):
                try:
                    # Save file
                    file_path = os.path.join("data", uploaded_file.name)
                    os.makedirs("data", exist_ok=True)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Process document
                    processor = DocumentProcessor()
                    text = processor.extract_text(file_path)
                    
                    # Store in session
                    st.session_state.current_doc = {
                        "name": uploaded_file.name,
                        "text": text,
                        "timestamp": datetime.now().isoformat()
                    }
                    
                    st.success("Document processed successfully!")
                    st.info(f"Extracted {len(text)} characters")
                except Exception as e:
                    st.error(f"Error processing document: {str(e)}")
    
    elif feature == "📝 Summarize":
        st.markdown('<h2 class="section-title">📝 Generate Summary</h2>', unsafe_allow_html=True)
        
        if st.session_state.current_doc:
            st.info(f"📄 Current Document: {st.session_state.current_doc['name']}")
            
            if st.button("✨ Generate Summary"):
                try:
                    generator = AIGenerator()
                    summary = generator.generate_summary(st.session_state.current_doc["text"])
                    st.subheader("Summary")
                    st.write(summary)
                    
                    # Download option
                    st.download_button("⬇️ Download Summary", summary, "summary.txt")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.error("❌ Please upload a document first in 'Upload Document' section")
    
    elif feature == "📋 Generate Notes":
        st.markdown('<h2 class="section-title">📋 Generate Notes</h2>', unsafe_allow_html=True)
        
        if st.session_state.current_doc:
            st.info(f"📄 Current Document: {st.session_state.current_doc['name']}")
            
            if st.button("✨ Generate Notes"):
                try:
                    generator = AIGenerator()
                    notes = generator.generate_notes(st.session_state.current_doc["text"])
                    st.subheader("Notes")
                    st.write(notes)
                    
                    st.download_button("⬇️ Download Notes", notes, "notes.txt")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.error("❌ Please upload a document first in 'Upload Document' section")
    
    elif feature == "❓ Q&A":
        st.markdown('<h2 class="section-title">❓ Document Q&A</h2>', unsafe_allow_html=True)
        
        if st.session_state.current_doc:
            st.info(f"📄 Current Document: {st.session_state.current_doc['name']}")
            question = st.text_input("Ask a question about the document")
            
            if question and st.button("🔍 Get Answer"):
                try:
                    generator = AIGenerator()
                    answer = generator.answer_question(st.session_state.current_doc["text"], question)
                    st.subheader("Answer")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.error("❌ Please upload a document first in 'Upload Document' section")
    
    elif feature == "📚 History":
        st.markdown('<h2 class="section-title">📚 History</h2>', unsafe_allow_html=True)
        
        try:
            response = requests.get(f"{API_URL}/history", headers={"user_id": st.session_state.user["id"]})
            if response.status_code == 200:
                history = response.json()
                for item in history:
                    st.write(f"📄 {item['filename']} - {item['timestamp']}")
            else:
                st.info("No history found")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Main logic - Enforce login requirement
if st.session_state.user is None:
    login_page()
else:
    main_app()
