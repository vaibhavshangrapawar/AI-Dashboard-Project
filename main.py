from fastapi import FastAPI
from data import projects, tasks, comments

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "API running"}

@app.get("/projects")
def get_projects():
    return projects

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/comments")
def get_comments():
    return comments