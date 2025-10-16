# tests/functional/test_forms_livre.py
from decimal import Decimal
from monApp import app, db
from monApp.models import Livre
from monApp.tests.functional.test_routes_livre import login


def test_livre_save_success(client, testapp):
    with app.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        old_title = livre.Titre

    login(client, "CDAL", "AIGRE", "/livre/save/")
    resp = client.post(
        "/livre/save/",
        data={"idL": 1, "Titre": "Les Misérables (test)", "Prix": "25.50", "AuteurId": "1"},
        follow_redirects=True,
    )

    assert resp.status_code == 200
    assert "/livres/1/view/" in resp.request.path
    assert b"Les Mis" in resp.data  

    with app.app_context():
        livre = Livre.query.get(1)
        assert livre.Titre == "Les Misérables (test)"
        assert round(Decimal(str(livre.Prix)), 2) == Decimal("25.50")


def test_livre_save_validation_error(client, testapp):
    with app.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        original_title = livre.Titre

    login(client, "CDAL", "AIGRE", "/livre/save/")
    resp = client.post(
        "/livre/save/",
        data={"idL": 1, "Titre": "Titre qui ne sera PAS sauvé", "AuteurId": "1"},
        follow_redirects=True,
    )

    assert resp.status_code == 200
    with app.app_context():
        livre = Livre.query.get(1)
        assert livre.Titre == original_title



def test_index_without_params(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Cricri' in resp.data


def test_index_with_params(client):
    resp = client.get('/index/?name=Toto')
    assert resp.status_code == 200
    assert b'Toto' in resp.data


def test_about_page(client):
    resp = client.get('/about/')
    assert resp.status_code == 200
    assert b'<!DOCTYPE html' in resp.data or b'<html' in resp.data


def test_contact_page(client):
    resp = client.get('/contact/')
    assert resp.status_code == 200
    assert b'<!DOCTYPE html' in resp.data or b'<html' in resp.data


def test_logout_redirects_to_index(client):
    login(client, "CDAL", "AIGRE", "/")
    resp = client.get('/logout/', follow_redirects=True)
    assert resp.status_code == 200
    assert b'Cricri' in resp.data
