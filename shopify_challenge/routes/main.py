from flask import jsonify

from shopify_challenge.extensions import home_view, register_view, login_view

def register_main_routes(app):
    app.add_url_rule('/', view_func=home_view, methods=['GET'])
    app.add_url_rule('/register', view_func=register_view, methods=['POST', 'GET'])
    #app.add_url_rule('/users/<string:username>', view_func=register_view, methods=['GET'])
    app.add_url_rule('/login', view_func=login_view, methods=['POST', 'GET'])