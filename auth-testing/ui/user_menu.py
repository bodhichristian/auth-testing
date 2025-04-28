from ui import user_flows as uf
from ui import task_flows as tf
from tasks import task_manager as tm

# this is a reminder to refactor the above modules

def user_menu(user):
    while True:
        uf.show_user_menu(user)
        choice = input('Select an option: ')

        if choice == '1':
            if confirm('change your password'):
                uf.change_password_flow(user)

        elif choice == '2':
            if confirm('delete your account'):
                uf.delete_account_flow(user)
                break

        elif choice == '3':
            tf.show_task_menu(user)

        elif choice == '4':
            uf.apply_for_admin_flow(user)

        elif choice == '5':
            if confirm('log out'):
                print('👋 Logged out.')
                break
        else:
            print('Please select one of the available options.')

