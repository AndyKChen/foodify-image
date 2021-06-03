import os

from flask import jsonify, redirect
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


def register_util_routes(app):
    @app.route("/health")
    def health():
        return {'status': 'Healthy!'}
    
    SWAGGER_URL = '/api/docs'
    API_URL = str(os.environ.get('HOST_NAME')) + '/spec'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "shopify-challenge"
        },
    )
    app.register_blueprint(swaggerui_blueprint)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Shopify Challenge"
        return jsonify(swag)

    @app.route("/")
    def reroute():
        return redirect("/discover/1")