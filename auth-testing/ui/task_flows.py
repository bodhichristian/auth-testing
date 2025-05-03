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
    column_widths = [20, 30, 10, 10, 10]
    rows = tm.get_task_table_data(user)
    print_table("Your tasks", headers, rows, column_widths)
    show_task_options()

def show_task_options():
    print('\n\nWhat would you like to do?')
    print('1. Mark a task complete')
    print('2. Edit a task')
    print('3. Delete a task')
    print('4. Back to Task Menu')

    while True:
        choice = input('Select an option: ')

        if choice == '1':
            # task completion logic
            print('\n\nfeaturecoming soon\n\n')
            continue

        elif choice == '2':
            # edit task logic
            print('\n\nfeaturecoming soon\n\n')
            continue

        elif choice == '3':
            # delete task logic
            print('\n\nfeaturecoming soon\n\n')
            continue

        elif choice == '4':
            continue

        else:
            print(f'\n\n❌ {choice} is not an available option\n\n')
            # show_task_options()
            continue