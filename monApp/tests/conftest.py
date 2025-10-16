# tests/conftest.py
import pytest
from hashlib import sha256

from monApp import app, db
from monApp.models import Auteur, Livre, User

@pytest.fixture
def testapp():
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })
    with app.app_context():
        db.create_all()

        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()

        livre = Livre(
            Titre="Les Misérables",
            Prix=19.99,
            Url="https://exemple.test/les-miserables",
            Img="https://exemple.test/les-miserables.jpg",
            auteur_id=auteur.idA
        )
        db.session.add(livre)

        m = sha256()
        m.update("AIGRE".encode())
        user = User(Login="CDAL", Password=m.hexdigest())
        db.session.add(user)

        db.session.commit()

        yield app

        db.drop_all()

@pytest.fixture
def client(testapp):
    return testapp.test_client()
