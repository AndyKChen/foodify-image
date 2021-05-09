from flask import session

from .helpers import login_test_user, register_test_user


def test_get_login_page(client):
    res = client.get('/login')
    assert res.status_code == 200


def test_valid_login(client):
    register_test_user(client)
    res = login_test_user(client)
    assert res.status_code == 301


def test_invalid_password_login(client):
    register_test_user(client)
    res = client.post('/login', data = {'username':'test_user',
                                        'password':'wrong_pw'})
    assert res.status_code == 401


def test_invalid_username_login(client):
    register_test_user(client)
    res = client.post('/login', data = {'username':'wrong_username',
                                        'password':'TestPw123'})
    assert res.status_code == 401