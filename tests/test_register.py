def test_get_register_page(client):
    res = client.get('/register')
    assert res.status_code == 200


def test_register_valid(client):
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'TestPw123'})
    assert res.status_code == 201


def test_register_invalid_password(client):
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'weakpw'})
    assert res.status_code == 400


def test_register_invalid_username(client):
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'TestPw123'})

    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'TestPw123'})
    assert res.status_code == 400

