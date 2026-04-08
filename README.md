#  AI Dashboard Project

##  Overview
This project is a Unified AI Dashboard that provides a structured view of projects and tasks along with an AI-powered chatbot for querying task-related information.

It integrates:
- Project overview
- Task drill-down
- Task details with comments
- AI chatbot (RAG-based)

---

##  Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **LLM**: Ollama (Llama3)
- **RAG**: Custom implementation using embeddings
- **Database**: JSON (mock data)
- **Tools**: VS Code, GitHub

---

##  Features

### 1️ Project Overview
- Tool Name
- Project Name
- Description
- Task Summary (ongoing, pending, completed)

### 2️ Project Drill-down
- Task Name
- Status (todo / in_progress / done / blocked)
- Assignee
- Priority
- Due Date
- Source Tool

### 3️ Task Details
- Detailed task info
- Threaded comments
- AI-generated insights

### 4️ AI Chatbot
- Ask queries like:
  - "Show ongoing tasks"
  - "What tasks are completed?"
  - "Any overdue tasks?"
- Uses RAG + Ollama for responses


---

## ⚙️ Setup Instructions

### Create Virtual Environment 
- python -m venv E2M
- E2M\Scripts\activate

### Run Backend (FastAPI)
- uvicorn main:app --reload

### Run Frontend (Streamlit)
- streamlit run app.py

### 1. Clone Repository
```bash
git clone https://github.com/vaibhavshangrapawar/AI-Dashboard-Project.git
cd AI-Dashboard-Project
