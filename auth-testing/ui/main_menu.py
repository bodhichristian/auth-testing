# ui/main_menu.py

import getpass

import auth.auth as auth
from auth.session import start_session
from auth.token import generate_token
from auth.auth import create_account, login, username_taken

def main_menu():
    while True:
        print('\n1. Create account')
        print('2. Log in')
        print('3. Exit')
        choice = input('Select an option: ')

        if choice == '1':
            handle_create_account()
        elif choice == '2':
            handle_login()
        elif choice == '3':
            print('✌️ Goodbye')
            break
        else:
            print('Please select one of the available options.')

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
        print('✅ Login successful.')
        token = generate_token(user.id)
        start_session(token)
    else:
        print('❌ Login failed.')