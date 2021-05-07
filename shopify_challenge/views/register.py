from flask import render_template, request, redirect, session, flash
from flask.views import MethodView
from passlib.hash import sha256_crypt

from shopify_challenge.helpers.validations import validate_new_user
from shopify_challenge.models.user import UserModel

class Register(MethodView):

    def post(self):
        session.clear()
        username = request.form.get("username")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        errors = validate_new_user(username, password)
        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template("register.html")

        password = sha256_crypt.hash((str)(password))

        user = UserModel(first_name=first_name,
                         last_name=last_name,
                         username=username,
                         password=password)
        try:
            user.save_to_database()
        except Exception:
            return {'message': 'An error occurred saving the user to the database.'}, 500
        
        flash('Account Created!', 'success')
        return redirect("login.html")


    # def post(self):
    #     request_data = self.request_parser.parse_args()
    #     errors = validate_new_user(request_data)
    #     if errors:
    #         return {'errors': errors}, 400

    #     password = sha256_crypt.hash((str)(request_data['password']))
        
    #     user = UserModel(first_name=request_data['first_name'],
    #                      last_name=request_data['last_name'],
    #                      username=request_data['username'],
    #                      password=password)
    #     try:
    #         user.save_to_database()
    #     except Exception:
    #         return {'message': 'An error occurred saving the user to the database.'}, 500
    #     return user.json(), 201

    def get(self):
        session.clear()
        return render_template("register.html")
    
    # def get(self, username):
    #     user = UserModel.find_by_username(username)
    #     if user is None:
    #         return {'message': 'This user does not exist'}, 404
    #     return user.json()