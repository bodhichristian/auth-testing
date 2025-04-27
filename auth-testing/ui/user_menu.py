from ui import user_flows as flow

def user_menu(user):
    while True:
        flow.show_main_menu(user)
        choice = input('Select an option: ')

        if choice == '1':
            if confirm('change your password'):
                flow.change_password_flow(user)

        elif choice == '2':
            if confirm('delete your account'):
                flow.delete_account_flow(user)
                break

        elif choice == '3':
            flow.apply_for_admin_flow(user)

        elif choice == '4':
            if confirm('log out'):
                print('👋 Logged out.')
                break
        else:
            print('Please select one of the available options.')

