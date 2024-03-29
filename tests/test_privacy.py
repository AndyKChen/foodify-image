from foodify.models.image import ImageModel

from .helpers import (edit_image, login_test_user, register_test_user,
                      upload_single_image)


def test_change_image_privacy(client):
    register_test_user(client)
    login_test_user(client)
    upload_single_image(client)

    private_images = ImageModel.get_private_images_by_username('test_user', 1)
    identifier = private_images.items[0].identifier
    assert private_images.items[0].private == True

    res = edit_image(client, identifier, 'make public')
    image = ImageModel.get_image_by_identifier(identifier)
    assert image.private == False
    assert res.status_code == 301

    # delete image from s3 and db
    edit_image(client, identifier, 'delete')