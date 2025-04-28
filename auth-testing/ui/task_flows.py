from models.user import User
from models.task import Task
from tasks import task_manager as tm

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
        tasks = tm._load_tasks()
        tasks[user.id] = task
        tm._save_tasks(tasks)
        break