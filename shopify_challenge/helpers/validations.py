import re

from shopify_challenge.models.user import UserModel

MIN_PW_LENGTH = 8

# Check for existing user and that password is valid
def validate_new_user(request_data):
    error_msgs = []
    password = request_data['password']
    if (UserModel.find_by_username(request_data['username']) is not None):
        error_msgs.append("Username already exists")
    if (len(password) < MIN_PW_LENGTH):
        error_msgs.append("Password must be at least 8 characters long")
    if not (re.search("[A-Z]", password)):
        error_msgs.append("Password must include a capital letter")
    if not (re.search("[0-9]", password)):
        error_msgs.append("Password must include a number")

    return error_msgs