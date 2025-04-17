from auth.auth import create_account, login, username_taken
import getpass

def main():
    while True:
        print('1. Create account')
        print('2. Log in')
        print('3. Exit')
        choice = input('Select an option: ')

        # Exit
        if choice == '3':
            print('✌️ Goodbye')
            break

        # Create account
        if choice == '1':
            while True:
                username = input('Create a username: ')
                if username_taken(username):
                    print('🚨 Username unavailable. Try again.')
                else:
                    break

            password = getpass.getpass('Create a password: ')
            if create_account(username, password):
                print('✅ Account created.')
            else:
                print('❌ Account not created.')

        # Log in
        elif choice == '2':
            username = input('Username  : ')
            password = getpass.getpass('Password: ')
            if login(username, password):
                print('✅ Login successful.')
            else:
                print('❌ Login failed.')

        else:
            print('Please select one of the available options.')

if __name__ == '__main__':
    main()