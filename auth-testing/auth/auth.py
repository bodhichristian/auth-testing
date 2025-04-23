import hashlib
import getpass
import json
import os
from models.user import User

USERS_FILE = "users.json"

def create_username():
    while True:
        username = input('Create a username: ')
        if not username:
            print('Please enter a username.')
            continue
        if username_taken(username):
            print('🚨 Username unavailable. Try again.')
            continue
        else:
            return username

def create_password():
    while True:
        pw1 = getpass.getpass('Create a password: ')
        pw2 = getpass.getpass('Confirm your password: ')

        if not pw1:
            print('❌ Password may not be left blank.')
            continue

        if pw1 != pw2:
            print('❌ Passwords do not match. Try again.')
            continue

        return pw1

def create_account(username, password):
    if not username or not password:
        return False

    password_hash = _hash_password(password)
    user = User(username, password_hash)

    users = _load_users()
    if username in users:
        return False

    users[username] = user
    _save_users(users)
    return True

def login(username, password):
    users = _load_users()
    hashed = _hash_password(password)
    user = users.get(username)
    if user and user.password_hash == hashed:
        return user
    return None

def change_password(user, current_password, new_password=None):
    users = _load_users()
    existing_user = users.get(user.username)

    if not existing_user or existing_user.password_hash != _hash_password(current_password):
        return False

    if new_password:
        existing_user.password_hash = _hash_password(new_password)
        _save_users(users)

    return True

def delete_account(username, password):
    users = _load_users()
    user = users.get(username)
    if user and user.password_hash == _hash_password(password):
        del users[username]
        _save_users(users)
        return True
    return False

def username_taken(username):
    users = _load_users()
    return username in users

def validate_user(id):
    users = _load_users()
    for user in users.values():
        if user.id == id:
            return user
    return None

# --- Internal Helpers ---
def _load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        try:
            users_data = json.load(f)
            # Convert dictionaries into User objects
            return {user_data["username"]: User.from_dict(user_data) for user_data in users_data}
        except json.JSONDecodeError:
            print('⚠️ [AUTH] Error: users.json cannot be read.')
            return {}

def _save_users(users):
    users_data = [user.to_dict() for user in users.values()]
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f)

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()