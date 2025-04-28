import os
import json
from models.task import Task

TASKS_FILE = 'tasks.json'

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

