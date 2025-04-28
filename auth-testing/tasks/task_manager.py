import os
import json
from models.task import Task

TASKS_FILE = 'tasks.json'

def show_task_menu(user):
    print('\nTasks')
    print('=====')
    print('1. Create a new task')
    print('2. View all tasks')
    print('3. Exit')

    choice = input('Select an option: ')
    if choice == '1':
        create_task_flow(user)
    if choice == '2':
        print('View all tasks feature coming soon.')
    if choice == '3':
        return

def create_task_flow(user):
    while True:
        print('\nCreate task')
        print('===========')

        title = input('Task title: ')
        description = input('Task description: ')

        task = Task(title=title, description=description, creator_id=user.id)
        tasks = _load_tasks()
        tasks[user.id] = task
        _save_tasks(tasks)
        break


# --- Internal Helpers ---
def _load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {}
    with open(TASKS_FILE, 'r') as f:
        try:
            task_data = json.load(f)
            return {task_data['id']: Task.from_dict(task_data) for task in task_data}
        except json.JSONDecodeError:
            print('⚠️ [AUTH] Error: tasks.json cannot be read.')
            return {}

def _save_tasks(tasks):
    task_data = [task.to_dict() for task in tasks.values()]
    with open(TASKS_FILE, 'w') as f:
        json.dump(task_data, f)

