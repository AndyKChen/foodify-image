from PIL import Image
import glob

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
    image_list = []
    file = TEST_IMAGES_PATH + 'apple.jpg'
    image_list.append(Image.open(file))
    res = client.post('/upload', data = {'uploaded_files':image_list, 
                                         'private':True})
    return res

def upload_multiple_images(client):
    image_list = []
    for filename in glob.glob(TEST_IMAGES_PATH + '*.jpg'): #assuming gif
        im=Image.open(filename)
        image_list.append(im)
    res = client.post('/upload', data = {'uploaded_files':image_list, 
                                         'private':True})
    return res