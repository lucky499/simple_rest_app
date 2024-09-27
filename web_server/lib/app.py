from gevent import monkey
monkey.patch_all()

import connexion
from flask import jsonify

def create_app():
    """main function to create an app """
    
# Create the application instance
    app = connexion.App(__name__, specification_dir=".")

# Read the openapi.yaml file to configure the endpoints
    app.add_api('openapi.yaml')
    kwargs = {"port": 5555}
    print("starting the simple application")
    app.run(**kwargs)

if __name__ == "__main__":
    create_app()  # Using Connexion's built-in run mechanism