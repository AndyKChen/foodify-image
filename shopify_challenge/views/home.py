from flask.views import MethodView

class Home(MethodView):
    def get(self):
        return {"message": "Hello World!"}, 200