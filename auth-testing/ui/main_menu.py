# ui/main_menu.py

import ui.user_flows as flow

def main_menu():
    while True:
        flow.show_main_menu()
        choice = input('Select an option: ')

        if choice == '1':
            flow.handle_create_account()
        elif choice == '2':
            flow.handle_login()
        elif choice == '3':
            print('\n✌️ Goodbye\n')
            break
        else:
            print('Please select one of the available options.\n')
