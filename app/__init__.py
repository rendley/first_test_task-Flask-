from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager




basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='hfouewhfoiwefoquw'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# migration
# FLASK_APP=app && flask db init
migrate = Migrate(app, db)

# login
login_manager = LoginManager(app)
login_manager.login_view = "login"


from app import views
from app.books import views
from app.authors import views