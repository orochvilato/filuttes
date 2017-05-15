from flask import Flask
from flask import render_template
from .views.home import home
from .views.user import user

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')
# Now we can access the configuration variables via app.config["VAR_NAME"].
from .util import assets

app.register_blueprint(home)
app.register_blueprint(user)
