from flask import jsonify

from shopify_challenge.extensions import (discover_view, login_view,
                                          personal_view, register_view,
                                          upload_view)


def register_main_routes(app):
    app.add_url_rule('/', view_func=discover_view, methods=['GET', 'POST'])
    app.add_url_rule('/register', view_func=register_view, methods=['POST', 'GET'])
    #app.add_url_rule('/users/<string:username>', view_func=register_view, methods=['GET'])
    app.add_url_rule('/login', view_func=login_view, methods=['POST', 'GET'])
    app.add_url_rule('/upload', view_func=upload_view, methods=['POST', 'GET'])
    app.add_url_rule('/personal/<int:page_num>', view_func=personal_view, methods=['GET', 'POST'])