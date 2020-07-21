#imports
from flask import Flask
from flask import redirect,render_template,url_for
from flask_wtf.csrf import CSRFProtect, CSRFError
from flask_bootstrap import Bootstrap



def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
      ))
    bootstrap = Bootstrap(app)

    from .models import item

    @app.route('/')
    def home():
        return render_template('home/index.html')
        
    from .views.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app