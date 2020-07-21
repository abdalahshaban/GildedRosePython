#imports
from flask import Flask



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    from .models import item

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
        
    # from .home import home as home_blueprint
    # app.register_blueprint(home_blueprint)

    return app