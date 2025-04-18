# ui/menu.py

import getpass
from ui.session import start_session
from auth.auth import create_account, login, username_taken

def show_menu():
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
    while True:
        username = input('Create a username: ')
        if not username:
            print('Please enter a username.')
        if username_taken(username):
            print('🚨 Username unavailable. Try again.')
        else:
            break

    while True:
        pw1 = getpass.getpass('Create a password: ')
        pw2 = getpass.getpass('Confirm your password: ')
        if not pw1:
            print('Password may not be left blank.')
        if pw1 != pw2:
            print('❌ Passwords do not match. Try again.')
        else:
            break

    if create_account(username, pw1):
        print('✅ Account created.')
    else:
        print('❌ Account not created.')

    pw1 = pw2 = None # Clear from memory

def handle_login():
    username = input('Username  : ')
    password = getpass.getpass('Password: ')
    if login(username, password):
        print('✅ Login successful.')
        start_session(username)
    else:
        print('❌ Login failed.')