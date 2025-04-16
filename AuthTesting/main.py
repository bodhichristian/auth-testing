from auth.auth import create_account, login
import getpass

def main():
    print('1. Create account')
    print('2. Log in')
    choice = input('Select an option: ')

    username = input('Username: ')
    password = getpass.getpass('Password: ')

    if choice == '1':
        if create_account(username, password):
            print('✅ Account created.')
        else:
            print('🚨 Username unavailable.')

    elif choice == '2':
        if login(username, password):
            print('✅ Login successful.')
        else:
            print('❌ Login failed.')

    else:
        print('Please select one of the available options.')

if __name__ == '__main__':
    main()