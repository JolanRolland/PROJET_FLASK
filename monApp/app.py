from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap5 import Bootstrap

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object("config")

# Initialisation des extensions
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

# Import des vues à la fin
from monApp import views
