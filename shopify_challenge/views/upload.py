from flask import redirect, render_template, session
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required


class Upload(MethodView):

    @login_required
    def get(self):
        return render_template("upload.html")

