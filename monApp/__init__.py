from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

# Import des routes
import monApp.views
