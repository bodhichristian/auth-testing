from models.user import User
from models.task import Task
from tasks import task_manager as tm
from ui.format.table import print_table

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

        tm.create_task(title, description, user.id)
        break

def display_assigned_tasks(user):
    headers = ['Title', 'Description', 'Created On', 'Due Date', 'Completed']
    column_widths = [20, 30, 15, 15, 10]
    rows = tm.get_task_table_data(user)
    print_table("Your tasks", headers, rows, column_widths)