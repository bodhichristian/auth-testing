import hashlib
import json
import os
from models.user import User

USERS_FILE = "users.json"

def _load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        try:
            users_data = json.load(f)
            # Convert dictionaries into User objects
            return {user_data["username"]: User.from_dict(user_data) for user_data in users_data}
        except json.JSONDecodeError:
            return {}

def _save_users(users):
    users_data = [user.to_dict() for user in users.values()]
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f)

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(username, password):
    users = _load_users()
    if username in users:
        return False

    password_hash = _hash_password(password)
    user = User(username, password_hash)
    users[username] = user
    _save_users(users)
    return True

def login(username, password):
    users = _load_users()
    hashed = _hash_password(password)
    user = users.get(username)
    return user and user.password_hash == hashed

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