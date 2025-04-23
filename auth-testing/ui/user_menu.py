from auth.auth import delete_account, change_password
import getpass

def user_menu(user):
    while True:
        print(f'\nWelcome, {user.username}!')
        print(f'Account holder since {user.created_on.strftime("%B %d, %Y").replace(" 0", " ")}\n')
        print('Menu')
        print('1. Change password')
        print('2. Delete account')
        print('3. Log out\n')

        choice = input('Select an option: ')

        if choice == '1':
            confirm = input('Are you sure you want to change your password? (y/n): ')
            if confirm.lower() == 'y':
                current = getpass.getpass('Enter current password: ')
                # Validate current password before continuing
                if not change_password(user, current, None):
                    print('❌ Current password incorrect.')
                    continue

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

                # Update password now that it's confirmed valid
                if change_password(user, current, new1):
                    print('✅ Password changed successfully.')
                else:
                    print('❌ Failed to update password.')

        elif choice == '2':
            confirm = input('Are you sure you want to delete your account? (y/n): ')
            if confirm.lower() == 'y':
                password = getpass.getpass('Confirm your password: ')
                if delete_account(user.username, password):
                    print('🗑️ Account deleted.')
                    break
                else:
                    print('❌ Incorrect password. Account not deleted.')

        elif choice == '3':
            print('👋 Logged out.')
            break

        else:
            print('Please select one of the available options.')