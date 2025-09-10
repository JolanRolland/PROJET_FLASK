from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

# Create database connection object
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
db.init_app(app)