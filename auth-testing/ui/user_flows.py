import getpass
import auth.auth as auth
from auth.session import start_session
from auth.token import generate_token

def handle_create_account():
    print('\nCreate account')
    print('=============')
    username = auth.create_username()
    password = auth.create_password()

    if auth.create_account(username, password):
        print('\n\n✅ Account created.')
    else:
        print('❌ Account not created. Please try again.')

    password = None # Clear from memory

def handle_login():
    print('\nLogin')
    print('=====')
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    user = auth.login(username, password)

    if user:
        print('\n🔑 Login successful.')
        token = generate_token(user.id)
        start_session(token)
    else:
        print('\n❌ Login failed.')

def confirm(action_name):
    confirm = input(f'Are you sure you want to {action_name}? (y/n): ')
    return confirm.lower() == 'y'

def change_password_flow(user):
    print('\nChanging password')
    print('======================')
    current = getpass.getpass('Enter current password: ')

    if not change_password(user, current, None):
        print('❌ Current password incorrect.')
        return

    while True:
        new1 = getpass.getpass('Enter new password: ')
        new2 = getpass.getpass('Confirm new password: ')
        if not new1:
            print('❌ Password may not be blank.')
            continue
        if new1 != new2:
            print('❌ Passwords do not match.')
            continue
        break

    if change_password(user, current, new1):
        print('\n✅ Password changed successfully.')
    else:
        print('❌ Failed to update password.')

def delete_account_flow(user):
    password = getpass.getpass('Confirm your password: ')
    if delete_account(user.username, password):
        print('🗑️ Account deleted.')
    else:
        print('❌ Incorrect password. Account not deleted.')

def apply_for_admin_flow(user):
    print('\nApply for administrator account')
    print('===============================\n')
    print('1. Request account upgrade')
    print('2. Exit\n')
    choice = input('Select an option: ')

    if choice == '1':
        print('📬 Request for administrator account submitted.')
    elif choice == '2':
        print('Returning to main menu.')


