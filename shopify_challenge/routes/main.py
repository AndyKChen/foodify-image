from flask import jsonify

from shopify_challenge.extensions import home_view
from shopify_challenge.extensions import user_view

def register_main_routes(app):
    app.add_url_rule('/', view_func=home_view, methods=['GET'])
    app.add_url_rule('/users', view_func=user_view, methods=['POST'])
    app.add_url_rule('/users/<string:username>', view_func=user_view, methods=['GET'])