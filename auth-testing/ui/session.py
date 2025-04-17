from auth.auth import delete_account
import getpass

def start_session(username):
    while True:
        print(f'\nWelcome, {username}!')
        print('1. Delete account')
        print('2. Log out')

        choice = input('Select an option: ')

        if choice == '1':
            confirm = input('Are you sure you want to delete your account? (y/n): ')
            if confirm.lower() == 'y':
                password = getpass.getpass('Confirm your password: ')
                if delete_account(username, password):
                    print('🗑️ Account deleted.')
                    break
                else:
                    print('❌ Incorrect password. Account not deleted.')

        elif choice == '2':
            print('👋 Logged out.')
            break

        else:
            print('Please select one of the available options.')