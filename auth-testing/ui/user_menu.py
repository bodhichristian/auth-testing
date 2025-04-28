from ui import user_flows as ux
from tasks import task_manager as tasks

# this is a reminder to refactor the above modules

def user_menu(user):
    while True:
        ux.show_user_menu(user)
        choice = input('Select an option: ')

        if choice == '1':
            if confirm('change your password'):
                ux.change_password_flow(user)

        elif choice == '2':
            if confirm('delete your account'):
                ux.delete_account_flow(user)
                break

        elif choice == '3':
            tasks.show_task_menu(user)

        elif choice == '4':
            ux.apply_for_admin_flow(user)

        elif choice == '5':
            if confirm('log out'):
                print('👋 Logged out.')
                break
        else:
            print('Please select one of the available options.')

