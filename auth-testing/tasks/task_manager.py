import os
import json
from models.task import Task

TASKS_FILE = 'tasks.json'

def create_task(title, description, creator_id):
    task = Task(title=title, description=description, creator_id=creator_id)
    tasks = _load_tasks()
    tasks[task.id] = task
    _save_tasks(tasks)

def fetch_tasks_for(user):
    tasks = tm._load_tasks()
    user_tasks = [task for task in tasks.values() if task.creator_id == user.id]
    return user_tasks

# --- Internal Helpers ---
def _load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, 'r') as f:
        try:
            task_data = json.load(f)
            return {task['id']: Task.from_dict(task) for task in task_data}
        except json.JSONDecodeError:
            print('⚠️ [TASK] Error: tasks.json cannot be read.')
            return {}

def _save_tasks(tasks):
    task_data = [task.to_dict() for task in tasks.values()]
    with open(TASKS_FILE, 'w') as f:
        json.dump(task_data, f)

