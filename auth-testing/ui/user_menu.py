from ui import user_flows as uf
from ui import task_flows as tf
from tasks import task_manager as tm

def user_menu(user):
    while True:
        print(f'\nWelcome, {user.username}!')
        print(f'User since {user.created_on.strftime("%B %d, %Y").replace(" 0", " ")}\n')
        print('Menu')
        print('====')
        print('1. Tasks')
        print('2. Change password')
        print('3. Delete account')
        print('4. Apply for administrator account')
        print('5. Log out\n')
        choice = input('Select an option: ')

        if choice == '1':
            tf.show_task_menu(user)

        elif choice == '2':
            if confirm('change your password'):
                uf.change_password_flow(user)

        elif choice == '3':
            if confirm('delete your account'):
                uf.delete_account_flow(user)
                break

        elif choice == '4':
            uf.apply_for_admin_flow(user)

        elif choice == '5':
            if uf.confirm('log out'):
                print('👋 Logged out.')
                break
        else:
            print('Please select one of the available options.')