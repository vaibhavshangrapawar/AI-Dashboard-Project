import requests
from datetime import date
from data import tasks


def get_relevant_task(query):
    query = query.lower()
    result = []

    for task in tasks:
        status = task.get("status", "")
        due = task.get("due_date")

        if "ongoing" in query and status == "in_progress":
            result.append(
                f"{task.get('name')} - "
                f"{task.get('summary')} "
                f"(Due: {due}, Tool: {task.get('source_tool')})"
            )

        elif "done" in query and status == "done":
            result.append(
                f"{task.get('name')} - "
                f"{task.get('summary')} (Completed)"
            )

        elif "overdue" in query and status != "done":
            if due and date.fromisoformat(due) < date.today():
                result.append(
                    f"{task.get('name')} - "
                    f"{task.get('summary')} (Due: {due})"
                )

    return result


def get_answer(query):
    relevant_task = get_relevant_task(query)

    if not relevant_task:
        return "No relevant data found."

    context = "Tasks: " + ", ".join(relevant_task)

    prompt = f"""
    User Question: {query}

    Context: {context}

    Answer clearly and explain using summary, due date and tool."""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except requests.exceptions.ConnectionError:
        return "Ollama is not running. Start it with: ollama serve"
    except Exception as e:
        return f"Unexpected error: {str(e)}"