# ui/main_menu.py

import getpass

import auth.auth as auth
from auth.session import start_session
from auth.token import generate_token
from auth.auth import create_account, login, username_taken

def main_menu():
    while True:
        print('\nMain Menu')
        print('1. Create account')
        print('2. Log in')
        print('3. Exit\n')
        choice = input('Select an option: ')

        if choice == '1':
            handle_create_account()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            print('✌️ Goodbye\n')
            break
        else:
            print('Please select one of the available options.\n')

def handle_create_account():
    username = auth.create_username()
    password = auth.create_password()

    if create_account(username, password):
        print('\n\n✅ Account created.')
    else:
        print('❌ Account not created. Please try again.')

    password = None # Clear from memory

def handle_login():
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    user = login(username, password)

    if user:
        print('\n🔑 Login successful.')
        token = generate_token(user.id)
        print(f'{token}')
        start_session(token)
    else:
        print('\n❌ Login failed.')