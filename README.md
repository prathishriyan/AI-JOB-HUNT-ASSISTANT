# 🤖 AI Job Hunt Assistant

An AI-powered job assistant that helps job seekers analyze job postings, tailor resumes, and generate personalized outreach messages using multi-agent systems.

---

## 🚀 Features

- 🔍 Fetch real job postings (USAJobs API)
- 🧠 Multi-agent system using CrewAI
- 📊 Job Description Analysis
- 📄 Resume Summary Generation
- ✉️ Personalized Cover Letter Creation
- 📩 Outreach Message Generation (LinkedIn/Email)
- 📁 Resume Upload (TXT, PDF, DOCX)
- ⬇️ Download results directly from UI
- 🌐 Interactive Streamlit Web App

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Framework:** CrewAI
- **LLM:** Gemini / OpenAI (via LiteLLM)
- **APIs:** USAJobs API
- **Libraries:** pdfplumber, python-docx, dotenv

---


## 📂 Project Structure

- AI-JOB-HUNT-ASSISTANT/
- │── agents/
- │ ├── jd_analyst.py
- │ ├── resume_cl_agent.py
- │ ├── messaging_agent.py
│
│── utils/
│ └── config.py
│
│── orchestrator.py
│── streamlit_app.py
│── usajobs_api.py
│── requirements.txt
│── README.md



---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI-JOB-HUNT-ASSISTANT.git
cd AI-JOB-HUNT-ASSISTANT

```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt

```

### 4. Setup environment variables

#### Create a .env file:

GEMINI_API_KEY=your_api_key_here


### 5. Run the application


```bash
python -m streamlit run streamlit_app.py
```

---

## 🧠 How It Works

1. User enters job keyword & location  
2. Uploads resume (PDF/DOCX/TXT)  
3. System fetches job data from API  
4. CrewAI agents perform:
   - Job analysis  
   - Resume tailoring  
   - Cover letter generation  
   - Outreach message creation  
5. Results are displayed and downloadable  

---


## 🎯 Use Cases

- Students applying for internships  
- Job seekers targeting government roles  
- Professionals optimizing resumes  
- Automated job application assistance  

---

## 🔒 Security Note

- API keys are stored securely using `.env`  
- `.env` is excluded via `.gitignore`  

---

## 🚀 Future Enhancements

- 🌍 Indian job API integration (Naukri/Apify)  
- 📊 Resume scoring system  
- 🧠 AI job recommendation engine  
- 📥 PDF export for results  
- 🌐 Deployment on Streamlit Cloud  

---

## 👩‍💻 Author

**Prathiksha Shriyan**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share!

---

## 🔥 Requirements File

Generate `requirements.txt` using:

```bash
pip freeze > requirements.txt

