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

def test_create_account_with_blank_username():
    username = ''
    password = 'password'

    users = {}
    users[username] = auth.create_account(username, password)

    assert not auth.create_account(username, password)

def test_create_account_with_blank_password():
    username = 'userdude'
    password = ''

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

def test_login_with_nonexistent_username():
    username = 'brandnewuser'
    password = 'security'

    users = {}
    users[username] = auth.create_account(username, password)

    assert not auth.login(username, 'random')

def test_password_is_hashed():
    raw = 'password'
    hashed = auth._hash_password(raw)
    assert hashed != raw
    assert len(hashed) == 64 # SHA-256 length

def test_password_case_sensitivity():
    username = 'Chad'
    password ='Password'

    users = {}
    users[username] = auth.create_account(username, password)

    assert not auth.login(username, password.lower())
