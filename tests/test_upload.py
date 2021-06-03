from foodify.models.image import ImageModel

from .helpers import (edit_image, login_test_user, register_test_user,
                      upload_multiple_images, upload_single_image)


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
    private_images = ImageModel.get_private_images_by_username('test_user', 1)
    assert private_images.total == 1
    assert res.status_code == 301
    
    # delete image from s3 and db
    edit_image(client, private_images.items[0].identifier, 'delete')


def test_upload_multiple_images(client):
    register_test_user(client)
    login_test_user(client)
    res = upload_multiple_images(client)
    private_images = ImageModel.get_private_images_by_username('test_user', 1)
    assert private_images.total == 3
    assert res.status_code == 301

    # delete images from s3 and db
    for image in private_images.items:
        edit_image(client, image.identifier, 'delete')
