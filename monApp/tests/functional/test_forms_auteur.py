from monApp.models import Auteur
from monApp import db
from monApp.tests.functional.test_routes_auteur import login
def test_auteur_save_success(client, testapp):
    # Créer un auteur dans la base de données
    with testapp.app_context():
        auteur = Auteur(Nom="Ancien Nom")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA
        # simulation connexion user et soumission du formulaire
        response=login(client, "CDAL", "AIGRE", "/auteur/save/")
        response = client.post("/auteur/save/",
        data={"idA": idA,"Nom": "Alexandre Dumas"},
        follow_redirects=True)
        # Vérifier que la redirection a eu lieu vers /auteurs/<idA>/view/ et que le contenu
        # est correct
        assert response.status_code == 200
        assert f"/auteurs/{idA}/view/" in response.request.path
        assert b"Alexandre Dumas" in response.data # contenu de la page vue
        # Vérifier que la base a été mise à jour
        with testapp.app_context():
            auteur = Auteur.query.get(idA)
            assert auteur.Nom == "Alexandre Dumas"
  
def test_auteur_insert_success(client, testapp):
    """Test de la création d’un auteur  (POST)."""
    with testapp.app_context():
        before_count = Auteur.query.count()

    login(client, "CDAL", "AIGRE", "/auteur/insert/")
    response = client.post(
        "/auteur/insert/",
        data={"Nom": "George Sand"},
        follow_redirects=True,
    )

    assert response.status_code == 200

    with testapp.app_context():
        after_count = Auteur.query.count()
        assert after_count == before_count + 1

        expected_id = after_count  
        assert f"/auteurs/{expected_id}/view/" in response.request.path

        auteur = Auteur.query.get(expected_id)
        assert auteur is not None
        assert auteur.Nom == "George Sand"

    assert b"George Sand" in response.data


def test_auteur_erase_success(client, testapp):
    """Test de la suppression d’un auteur  (POST)."""
    with testapp.app_context():
        auteur = Auteur(Nom="Auteur Temporaire")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA

    login(client, "CDAL", "AIGRE", "/auteur/erase/")
    response = client.post(
        "/auteur/erase/",
        data={"idA": idA},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == "/auteurs/"
    assert b"Auteur Temporaire" not in response.data

    with testapp.app_context():
        auteur = Auteur.query.get(idA)
        assert auteur is None