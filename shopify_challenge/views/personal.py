from flask import render_template, session
from flask.views import MethodView

from shopify_challenge.helpers.decorators import login_required
from shopify_challenge.models.image import ImageModel

class Personal(MethodView):
    
    @login_required
    def get(self):
        # public_images = ImageModel.get_public_images_by_username(session['username'])
        # private_images = ImageMode.get_private_images_by_username(session['username'])
        return render_template("personal.html")