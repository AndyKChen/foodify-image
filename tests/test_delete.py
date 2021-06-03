from foodify.models.image import ImageModel

from .helpers import (edit_image, login_test_user, register_test_user,
                      upload_single_image)


def test_delete_image(client):
    register_test_user(client)
    login_test_user(client)
    upload_single_image(client)

    private_images = ImageModel.get_private_images_by_username('test_user', 1)
    assert private_images.total == 1

    res = edit_image(client, private_images.items[0].identifier, 'delete')
    print(res.status_code)
    private_images = ImageModel.get_private_images_by_username('test_user', 1)
    assert private_images.total == 0
    assert res.status_code == 301

    