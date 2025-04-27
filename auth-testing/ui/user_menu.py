from auth.auth import delete_account, change_password
import getpass

def user_menu(user):
    while True:
        show_main_menu(user)
        choice = input('Select an option: ')

        if choice == '1':
            if confirm('change your password'):
                change_password_flow(user)

        elif choice == '2':
            if confirm('delete your account'):
                delete_account_flow(user)
                break

        elif choice == '3':
            apply_for_admin_flow(user)

        elif choice == '4':
            if confirm('log out'):
                print('👋 Logged out.')
                break
        else:
            print('Please select one of the available options.')

def show_main_menu(user):
    print(f'\nWelcome, {user.username}!')
    print(f'User since {user.created_on.strftime("%B %d, %Y").replace(" 0", " ")}\n')
    print('Menu')
    print('====')
    print('1. Change password')
    print('2. Delete account')
    print('3. Apply for administrator account')
    print('4. Log out\n')

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