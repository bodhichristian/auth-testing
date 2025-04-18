import os
import pytest
import auth.auth as auth

@pytest.fixture(autouse=True)
def temp_users_file(tmp_path):
    original = auth.USERS_FILE
    test_file = tmp_path / "test_users.json"
    auth.USERS_FILE = str(test_file)
    yield
    auth.USERS_FILE = original
    if os.path.exists(test_file):
        os.remove(test_file)

def test_create_account():
    username = 'testuser'
    password = 'password'

    auth.create_account(username, password)
    assert auth.username_taken(username)

def test_create_account_with_existing_username():
    username = 'testuser'
    password = 'password'

    auth.create_account(username, password)
    assert not auth.create_account(username, password)

def test_create_account_with_blank_username():
    username = ''
    password = 'password'

    auth.create_account(username, password)
    assert not auth.create_account(username, password)

def test_create_account_with_blank_password():
    username = 'userdude'
    password = ''

    auth.create_account(username, password)
    assert not auth.create_account(username, password)

def test_login_with_correct_password():
    username = 'newuser'
    password = 'supersecure'
    auth.create_account(username, password)

    assert auth.login(username, password)

def test_login_fails_with_incorrect_password():
    username = 'newuser'
    password = 'supersecure'

    auth.create_account(username, password)
    assert not auth.login(username, 'random')

def test_login_with_nonexistent_username():
    username = 'brandnewuser'
    password = 'security'

    auth.create_account(username, password)

    assert not auth.login(username, 'random')

def test_password_is_hashed():
    raw = 'password'
    hashed = auth._hash_password(raw)
    assert hashed != raw
    assert len(hashed) == 64 # SHA-256 length

def test_password_case_sensitivity():
    username = 'Chad'
    password ='Password'

    auth.create_account(username, password)
    assert not auth.login(username, password.lower())

def test_account_deletion():
    username = 'supercooldude'
    password = 'password123'

    auth.create_account(username, password)

    assert auth.login(username, password)
    assert auth.delete_account(username, password)
    assert not auth.login(username, password)
