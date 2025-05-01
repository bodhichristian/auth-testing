# ui/main_menu.py

from ui.user_flows import handle_create_account, handle_login

def main_menu():
    while True:
        print('\nMain Menu')
        print('=========')
        print('1. Create account')
        print('2. Log in')
        print('3. Exit\n')
        choice = input('Select an option: ')

        if choice == '1':
            handle_create_account()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            print('\n✌️ Goodbye\n')
            break
        else:
            print('Please select one of the available options.\n')
