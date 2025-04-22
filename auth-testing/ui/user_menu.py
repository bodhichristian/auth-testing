from auth.auth import delete_account
import getpass

def user_menu(user):
    while True:
        print(f'\nWelcome, {user.username}!')
        print(f'Account holder since {user.created_on}\n')
        print('Menu')
        print('1. Delete account')
        print('2. Log out\n')

        choice = input('Select an option: ')

        if choice == '1':
            confirm = input('Are you sure you want to delete your account? (y/n): ')
            if confirm.lower() == 'y':
                password = getpass.getpass('Confirm your password: ')
                if delete_account(user.username, password):
                    print('🗑️ Account deleted.')
                    break
                else:
                    print('❌ Incorrect password. Account not deleted.')

        elif choice == '2':
            print('👋 Logged out.')
            break

        else:
            print('Please select one of the available options.')