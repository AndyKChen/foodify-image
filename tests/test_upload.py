from .helpers import register_test_user, login_test_user, upload_single_image, upload_multiple_images

def test_get_upload_page(client):
    register_test_user(client)
    login_test_user(client)
    res = client.get('/upload')
    assert res.status_code == 200


def test_get_upload_page_no_login(client):
    res = client.get('/upload')
    assert res.status_code == 302


def test_upload_single_image(client):
    register_test_user(client)
    login_test_user(client)
    res = upload_single_image(client)
    assert res.status_code == 201


def test_upload_multiple_images(client):
    register_test_user(client)
    login_test_user(client)
    res = upload_multiple_images(client)
    assert res.status_code == 201
