from ui.user_menu import user_menu
from auth.token import decode_token
from auth.auth import validate_user

def start_session(token):
    user_data = decode_token(token)
    if not user_data:
        print('❌ Invalid or expired session. Please log in again.')
        return

    print('✅ Token validated.')
    id = user_data['user_id']
    user = validate_user(id)

    if not user:
        print('❌ User not found.')
        return

    print('🎬 Starting session...')
    user_menu(user)



