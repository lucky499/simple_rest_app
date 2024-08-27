from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = 'openapi.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "simple_test_app"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Simple Resource
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}
class Health(Resource):
    def get(self):
        return 200


api.add_resource(HelloWorld, '/hello')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(debug=True)
