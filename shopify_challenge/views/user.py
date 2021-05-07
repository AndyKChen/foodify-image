from flask.views import MethodView
from flask_restful import reqparse
from passlib.hash import sha256_crypt

from shopify_challenge.helpers.validations import validate_new_user
from shopify_challenge.models.user import UserModel

class User(MethodView):
    request_parser = reqparse.RequestParser()
    request_parser.add_argument('first_name')
    request_parser.add_argument('last_name')
    request_parser.add_argument('username')
    request_parser.add_argument('password')

    def post(self):
        request_data = self.request_parser.parse_args()
        errors = validate_new_user(request_data)
        if errors:
            return {'errors': errors}, 400

        password = sha256_crypt.hash((str)(request_data['password']))
        
        user = UserModel(first_name=request_data['first_name'],
                         last_name=request_data['last_name'],
                         username=request_data['username'],
                         password=password)
        try:
            user.save_to_database()
        except Exception:
            return {'message': 'An error occurred saving the user to the database.'}, 500
        return user.json(), 201
    
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user is None:
            return {'message': 'This user does not exist'}, 404
        return user.json()