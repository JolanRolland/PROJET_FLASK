# tests/functional/test_routes_livre.py
from monApp import app


def test_livres_liste(client):
    resp = client.get('/livres/')
    assert resp.status_code == 200
    assert b'Les Mis' in resp.data 


def test_livre_view_no_login(client):
    resp = client.get('/livres/1/view/')
    assert resp.status_code == 200
    assert b'Les Mis' in resp.data


def test_livre_update_before_login(client):
    resp = client.get('/livres/1/update/', follow_redirects=False)
    assert resp.status_code == 302
    assert "/login/?next=%2Flivres%2F1%2Fupdate%2F" in resp.headers["Location"]

    resp = client.get('/livres/1/update/', follow_redirects=True)
    assert resp.status_code == 200
    assert b'Login' in resp.data


def login(client, username, password, next_path):
    return client.post(
        "/login/",
        data={"Login": username, "Password": password, "next": next_path},
        follow_redirects=True,
    )


def test_livre_update_after_login(client, testapp):
    with app.app_context():
        resp = login(client, "CDAL", "AIGRE", "/livres/1/update/")
        assert resp.status_code == 200
        assert b'Titre' in resp.data
        assert b'Prix' in resp.data
        assert b'Les Mis' in resp.data
