from .helpers import register_test_user, login_test_user, upload_single_image, upload_multiple_images, edit_image
from shopify_challenge.models.image import ImageModel

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
    private_images = ImageModel.get_private_images_by_username('test_user')
    assert len(private_images) == 1
    assert res.status_code == 201
    
    # delete image from s3 and db
    edit_image(client, private_images[0].identifier, 'delete')


def test_upload_multiple_images(client):
    register_test_user(client)
    login_test_user(client)
    res = upload_multiple_images(client)
    private_images = ImageModel.get_private_images_by_username('test_user')
    assert(len(private_images) == 3)
    assert res.status_code == 201

    # delete images from s3 and db
    for image in private_images:
        edit_image(client, image.identifier, 'delete')
