from .helpers import register_test_user, login_test_user, upload_single_image, edit_image
from shopify_challenge.models.image import ImageModel

def test_delete_image(client):
    register_test_user(client)
    login_test_user(client)
    upload_single_image(client)

    private_images = ImageModel.get_private_images_by_username('test_user')
    assert len(private_images) == 1

    res = edit_image(client, private_images[0].identifier, 'delete')

    private_images = ImageModel.get_private_images_by_username('test_user')
    assert len(private_images) == 0
    assert res.status_code == 200

    