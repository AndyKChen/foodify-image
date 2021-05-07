from flask import render_template, session, redirect
from flask.views import MethodView


class Discover(MethodView):
    def get(self):

        return render_template('discover.html')