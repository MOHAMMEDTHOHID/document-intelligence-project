# 🚀 Deployment Guide - Document Intelligence Platform

## Deployment Options

### **Option 1: Streamlit Cloud (EASIEST)**
Best for Streamlit frontend only

#### Steps:
1. **Push to GitHub** (✅ Already done)
   ```bash
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repo
   - Select branch: `main`
   - Select file path: `app/main.py`
   - Click "Deploy"

3. **Configure Backend URL**
   - In Streamlit app settings, add:
   - `API_URL = "http://your-backend-url:8000"`

**Pros:** Free, easy, automatic updates from GitHub  
**Cons:** Only for frontend; need separate backend hosting

---

### **Option 2: Railway (RECOMMENDED)**
Hosts both frontend and backend

#### Prerequisites:
- GitHub account (already have ✅)
- Railway account (free at https://railway.app)

#### Setup Backend on Railway:

1. **Create `Procfile`**
   ```bash
   web: python -m uvicorn backend.api:app --host 0.0.0.0 --port $PORT
   ```

2. **Update `requirements.txt`** (already updated ✅)

3. **Create `railway.json`**
   ```json
   {
     "build": {
       "builder": "dockerfile"
     }
   }
   ```

4. **On Railway Dashboard:**
   - Click "New Project"
   - Select "Deploy from GitHub"
   - Select your repository
   - Configure environment variables
   - Deploy!

#### Setup Frontend on Railway:

1. **Create `streamlit_procfile`**
   ```bash
   web: streamlit run app/main.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Add to GitHub and deploy**

---

### **Option 3: Docker + Cloud Run (Google Cloud)**

#### Create `Dockerfile`:
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "backend.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Steps:
1. Install Google Cloud SDK
2. Create Google Cloud project
3. Build and push image:
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/doc-intelligence
   ```
4. Deploy to Cloud Run:
   ```bash
   gcloud run deploy doc-intelligence --image gcr.io/PROJECT_ID/doc-intelligence --platform managed
   ```

---

### **Option 4: Heroku (Legacy)**

#### Steps:
1. **Create `Procfile`**
   ```bash
   web: python -m uvicorn backend.api:app --host 0.0.0.0 --port $PORT
   ```

2. **Install Heroku CLI**
   ```bash
   npm install -g heroku
   ```

3. **Login & Deploy**
   ```bash
   heroku login
   heroku create doc-intelligence-platform
   git push heroku main
   ```

---

### **Option 5: DigitalOcean App Platform**

#### Steps:
1. Go to DigitalOcean
2. Create "App"
3. Connect GitHub repository
4. Configure:
   - Source: `backend/api.py`
   - Port: `8000`
5. Add environment variables
6. Deploy!

---

## Quick Deployment Checklist

### Before Deploying:

- [ ] Update API_URL in `app/main.py` to production backend URL
- [ ] Create `.env` file with production secrets
- [ ] Test locally first
- [ ] All changes pushed to GitHub
- [ ] Create `requirements.txt` (✅ Done)
- [ ] Database setup (if needed)

### Environment Variables to Set:

```
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-api-key
```

---

## Recommended Path: Railway

### Step-by-step for Railway:

1. **Go to railway.app**
   - Sign up with GitHub
   
2. **New Project → Deploy from GitHub**
   - Select `MOHAMMEDTHOHID/document-intelligence-project`

3. **Configure:**
   - Build: Automatic
   - Start Command: `python -m uvicorn backend.api:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables:**
   - Port: 8000
   - Any other secrets needed

5. **Get Public URL**
   - Railway gives you URL like: `https://doc-intelligence-project.up.railway.app`

6. **Update Streamlit app to use this URL**

---

## After Deployment

1. **Test endpoints:**
   ```bash
   curl https://your-deployed-url.com/docs
   ```

2. **Update Streamlit to use production backend**

3. **Deploy Streamlit to Streamlit Cloud** using same process

4. **Test full workflow**
   - Signup → Login → Upload → Summarize

---

## Troubleshooting

### Issue: "Cannot connect to backend"
- Check API_URL in app/main.py
- Verify backend is running
- Check CORS settings in backend

### Issue: "Port already in use"
- Change port in environment variables
- Use: `--port $PORT` for cloud

### Issue: "Module not found"
- Ensure all packages in requirements.txt
- Check Python version matches (3.8+)

---

## Free Alternatives

| Service | Free Tier | Best For |
|---------|-----------|----------|
| **Streamlit Cloud** | Yes | Frontend |
| **Railway** | $5/month | Backend + Frontend |
| **Render** | Yes (limited) | Full stack |
| **PythonAnywhere** | Yes | Python apps |
| **Google Cloud Run** | $2.50/month | Containerized apps |

---

## Next Steps

1. Choose deployment platform
2. Create necessary config files
3. Push to GitHub
4. Follow platform-specific setup
5. Test deployed app
6. Update documentation

Questions? Check platform's documentation!
