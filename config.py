import os
import random
import string

SECRET_KEY = "1cb282d9-4ccd-4c47-a0da-edf29219afc1"

ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Page contact : vous pouvez nous écrire sur contact@tutoflask.fr"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "monApp.db")

BOOTSTRAP_SERVE_LOCAL = True