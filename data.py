projects = [
    {
        "id": 1,
        "name" : "website revamp", 
        "tool": "Trello", 
        "description": "Website redesign",
        "task_summary": {
            "ongoing": 1,
            "pending": 1,
            "completed" : 0
        }
    },
    {
        "id": 2 ,
        "name" : "Marketing campaign", 
        "tool" : "Asana", 
        "description" : "Ad campaign",
        "task_summary": {
            "ongoing": 0,
            "pending": 0,
            "completed": 1
        }
        },
]


tasks = [
    {
        "id" : 1,
        "project_id":1,
        "name" : "Fix login bug",
        "summary": "Resolve login API issue",
        "Status" : "in_progress",
        "assignee": "John",
        "Priority" : "High",
        "Due date" : "2026-04-10",
        "Source tool" : "Trello",
    },
    {
        "id" : 2,
        "project_id":1,
        "name" : "Deploy backend",
        "summary": "Deploy backend to production",
        "Status" : "todo",
        "assignee": "alice",
        "Priority" : "Medium",
        "Due date" : "2026-04-12",
        "Source tool" : "Trello",
    },
    {
        "id" : 3,
        "project_id": 2,
        "name" : "Update UI",
        "summary": "Improve UI",
        "Status" : "Done",
        "assignee": "Bob",
        "Priority" : "Low",
        "Due date" : "2026-04-05",
        "Source tool" : "Trello",},

]

comments = [
    {   "task_id": 1,
        "user" : "John",
        "text": "API failing"},

    {   "task_id": 1,
        "user" : "Alice",
        "text": "Investigation"},

    {
        "task_id": 1,
        "user" : "John",
        "text": "Fix before release"}
]

