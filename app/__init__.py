#imports
from flask import Flask
from flask import redirect,render_template,url_for



def create_app():
    app = Flask(__name__)

    from .models import item

    @app.route('/')
    def home():
        return render_template('home/index.html')
        
    from .views.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app