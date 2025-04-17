import hashlib
import json
import os


USERS_FILE = "users.json"

def _load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def _save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account(username, password):
    users = _load_users()
    if username in users:
        return False
    users[username] = _hash_password(password)
    _save_users(users)
    return True

def login(username, password):
    users = _load_users()
    hashed = _hash_password(password)
    return users.get(username) == hashed

def username_taken(username):
    users = _load_users()
    return username in users