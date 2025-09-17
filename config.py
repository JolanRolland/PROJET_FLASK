import os
import random
import string

SECRET_KEY = "".join([random.choice(string.printable) for _ in os.urandom(24)])

ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Page contact : vous pouvez nous écrire sur contact@tutoflask.fr"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "monApp.db")
