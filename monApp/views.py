from .app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="Accueil", name="Cricri")

@app.route('/about/')
def about():
    return render_template("about.html", title="À propos", message=app.config["ABOUT"], name="Cricri")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title="Contact", message=app.config["CONTACT"], name="Cricri")
