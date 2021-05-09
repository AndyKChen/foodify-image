from .helpers import register_test_user


def test_get_register_page(client):
    res = client.get('/register')
    assert res.status_code == 200


def test_register_valid(client):
    res = register_test_user(client)
    assert res.status_code == 301


def test_register_invalid_password(client):
    register_test_user(client)
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'weakpw'})
    assert res.status_code == 400


def test_register_invalid_username(client):
    register_test_user(client)
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'TestPw123'})
    assert res.status_code == 400

