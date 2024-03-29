from flask import flash, redirect, render_template, request, session
from flask.views import MethodView

from foodify.helpers.validations import validate_user
from foodify.models.user import UserModel


class Login(MethodView):

    def post(self):
        session.clear()
        username = request.form.get("username")
        password = request.form.get("password")

        error = validate_user(username, password)
        if error:
            flash(error, 'danger')
            return render_template("login.html"), 401
        
        session["username"] = username
        session.permanent = True

        return redirect("/personal/1"), 301
    
    def get(self):
        session.clear()
        return render_template("login.html"), 200