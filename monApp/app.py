from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap5 import Bootstrap

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object("config")

from flask_login import LoginManager
login_manager = LoginManager(app)

# Initialisation des extensions
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

login_manager.login_view = "login"

# Import des vues à la fin
from monApp import views
