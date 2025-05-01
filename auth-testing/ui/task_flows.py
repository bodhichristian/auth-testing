from models.user import User
from models.task import Task
from tasks import task_manager as tm

def show_task_menu(user):
    print('\nTasks')
    print('=====')
    print('1. Create a new task')
    print('2. View assigned tasks')
    print('3. Exit')

    choice = input('Select an option: ')
    if choice == '1':
        create_task_flow(user)
    if choice == '2':
        display_assigned_tasks(user)
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

def display_assigned_tasks(user):
    tasks = tm._load_tasks()
    user_tasks = [task for task in tasks.values() if task.creator_id== user.id]

    headers = ['Title', 'Description', 'Created On', 'Due Date', 'Completed']
    column_widths = [20, 30, 15, 15, 10]

    # row formatter
    def format_row(items):
        return "| " + " | ".join(f"{str(item)[:width]:<{width}}" for item, width in zip(items, column_widths)) + " |"

    # title
    print('\n\nYour tasks')
    print('==========')

    # header row
    print("-" * (sum(column_widths) + len(column_widths) * 3 + 1))
    print(format_row(headers))
    print("-" * (sum(column_widths) + len(column_widths) * 3 + 1))

    # task list
    for task in user_tasks:
        due = task.due_date if task.due_date else "N/A"
        complete = 'Y' if task.completed else 'N'
        print(format_row([task.title, task.description, task.created_on, due, complete]))

    # Bottom border
    print("-" * (sum(column_widths) + len(column_widths) * 3 + 1))