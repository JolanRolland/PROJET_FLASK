from monApp.models import Livre

def test_livre_init(testapp):
    livre = Livre(
        Titre="Notre-Dame de Paris",
        Prix=12.5,
        Url="https://exemple.test/notre-dame",
        Img="https://exemple.test/notre-dame.jpg",
        auteur_id=1
    )
    assert livre.Titre == "Notre-Dame de Paris"
    assert isinstance(livre.Prix, float)
    assert livre.auteur_id == 1

def test_livre_repr(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"

def test_livre_relation_auteur(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        assert livre.auteur is not None
        assert livre.auteur.Nom == "Victor Hugo"
