import glob

from shopify_challenge.models.image import ImageModel

TEST_IMAGES_PATH = 'tests/test_images/'

def register_test_user(client):
    res = client.post('/register', data = {'first_name':'test', 
                                           'last_name':'user', 
                                           'username':'test_user',
                                           'password':'TestPw123'})
    return res

def login_test_user(client):
    res = client.post('/login', data = {'username':'test_user',
                                        'password':'TestPw123'})
    return res

def upload_single_image(client):
    path = TEST_IMAGES_PATH + 'single_image/apple.jpg'
    res = client.post(
            '/upload', # flask route
            data={'file': [open(path, 'rb')],
                'access_type':'private'}
            )
    return res

def upload_multiple_images(client):
    path = TEST_IMAGES_PATH + 'multiple_images/*.jpg'
    image_list = []

    for filename in glob.glob(path): 
        im = open(filename, 'rb')
        image_list.append(im)

    res = client.post(
            '/upload', # flask route
            data={'file': image_list,
                'access_type':'private'}
            )
    return res

def edit_image(client, identifier, action):
    res = client.post('/personal', data={'action':action, 'identifier':identifier})
    return res