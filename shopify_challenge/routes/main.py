from flask import jsonify

from shopify_challenge.extensions import home_view

def register_main_routes(app):
    app.add_url_rule('/', view_func=home_view, methods=['GET'])