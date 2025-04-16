import auth.auth as auth

def test_create_account():
    username = 'testuser'
    password = 'password'

    users = {}
    users[username] = auth._hash_password(password)

    assert username in users

def test_create_account_with_existing_username():
    username = 'testuser'
    password = 'password'

    users = {}
    users[username] = auth.create_account(username, password)

    assert not auth.create_account(username, password)

def test_login_with_correct_password():
    username = 'newuser'
    password = 'supersecure'

    users = {}
    users[username] = auth.create_account(username, password)

    assert auth.login(username, password)

def test_login_with_incorrect_password():
    username = 'newuser'
    password = 'supersecure'

    users = {}
    users[username] = auth.create_account(username, password)

    assert not auth.login(username, 'random')
