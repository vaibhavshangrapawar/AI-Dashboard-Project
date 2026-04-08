import streamlit as st
import requests
from rag import get_answer

st.set_page_config(page_title="AI Dashboard", layout="wide")
st.title("Unified Project Intelligence Dashboard")

projects = requests.get("http://127.0.0.1:8000/projects").json()

tasks = requests.get("http://127.0.0.1:8000/tasks").json()

comments = requests.get("http://127.0.0.1:8000/comments").json()

# PROJECT OVERVIEW
st.header("Projects Overview")

for p in projects:
    st.subheader(f"{p['name']} ({p['tool']})")
    st.write("Discription:", p["description"])

    summary = p.get("task_summary",
                    {"ongoing":0,"pending":0,"completed":0})

# PROJECT DRILL-DOWN
st.header("Project Drill-down")

project_names = [p["name"] for p in projects]
selected_project = st.selectbox("Select Project", project_names)

selected_project_id = next(p["id"] for p in projects if p["name"] == selected_project)
filtered_tasks = [t for t in tasks if t ["project_id"] == selected_project_id]

for t in filtered_tasks:
    st.write(f"""
    **{t.get('name')}**
    - Summary: {t.get('summary')}
    - Status: {t.get('status')}
    - Assignee: {t.get('assignee')}
    - Priority: {t.get('priority')}
    - Due Date: {t.get('due_date')}
    - Source Tool: {t.get('source_tool')}
    """

    )

# TASK COMMENTS
st.header("Task Details")

task_names = [t.get("name") for t in tasks]
selected_task = st.selectbox("Select Task",task_names)

selected_task_id = next(t["id"] for t in tasks if t["name"] == selected_task)

task_comments = [c for c in comments if c["task_id"] == selected_task_id]

for c in task_comments:
    st.write(f"{c['user']} : {c['text']}")


# CHATBOT

st.header("AI Chatbot")

query = st.text_input("Ask something")

if query:
    response = get_answer(query)
    st.success(response)



