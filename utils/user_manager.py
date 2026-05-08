import os
import json
import hashlib
from pathlib import Path
from datetime import datetime

class UserManager:
    """Manage user accounts and authentication"""
    
    def __init__(self):
        self.users_dir = "users"
        self.users_file = os.path.join(self.users_dir, "users.json")
        self._ensure_dir()
        self._load_or_create_users()
    
    def _ensure_dir(self):
        """Ensure users directory exists"""
        os.makedirs(self.users_dir, exist_ok=True)
    
    def _load_or_create_users(self):
        """Load users from file or create empty"""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump([], f)
    
    def _hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _load_users(self):
        """Load users from file"""
        try:
            with open(self.users_file, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def _save_users(self, users):
        """Save users to file"""
        with open(self.users_file, 'w') as f:
            json.dump(users, f, indent=2)
    
    def create_user(self, email, password):
        """Create new user"""
        users = self._load_users()
        
        # Check if user already exists
        if any(u['email'] == email for u in users):
            return False
        
        user = {
            "id": str(len(users) + 1),
            "email": email,
            "password": self._hash_password(password),
            "created_at": datetime.now().isoformat(),
            "documents": []
        }
        
        users.append(user)
        self._save_users(users)
        
        # Create user's document history file
        user_doc_file = os.path.join(self.users_dir, f"{user['id']}_docs.json")
        with open(user_doc_file, 'w') as f:
            json.dump([], f)
        
        return True
    
    def authenticate_user(self, email, password):
        """Authenticate user credentials"""
        users = self._load_users()
        
        for user in users:
            if user['email'] == email and user['password'] == self._hash_password(password):
                return user
        
        return None
    
    def get_user(self, email):
        """Get user by email"""
        users = self._load_users()
        for user in users:
            if user['email'] == email:
                return user
        return None
    
    def update_user(self, user_id, **kwargs):
        """Update user information"""
        users = self._load_users()
        
        for i, user in enumerate(users):
            if user['id'] == user_id:
                for key, value in kwargs.items():
                    if key != 'password':  # Don't allow direct password update
                        user[key] = value
                users[i] = user
                break
        
        self._save_users(users)
    
    def add_document(self, user_id, document_info):
        """Add document to user's history"""
        users = self._load_users()
        
        for user in users:
            if user['id'] == user_id:
                user['documents'].append(document_info)
                break
        
        self._save_users(users)
    
    def get_user_documents(self, user_id):
        """Get all documents for user"""
        user_doc_file = os.path.join(self.users_dir, f"{user_id}_docs.json")
        
        if os.path.exists(user_doc_file):
            with open(user_doc_file, 'r') as f:
                return json.load(f)
        
        return []
    
    def delete_user(self, user_id):
        """Delete user account"""
        users = self._load_users()
        users = [u for u in users if u['id'] != user_id]
        self._save_users(users)
        
        # Delete user's documents file
        user_doc_file = os.path.join(self.users_dir, f"{user_id}_docs.json")
        if os.path.exists(user_doc_file):
            os.remove(user_doc_file)
