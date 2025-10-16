from hashlib import sha256
from monApp.models import User, load_user

def test_user_get_id(testapp):
    with testapp.app_context():
        user = User.query.get("CDAL")
        assert user is not None
        assert user.get_id() == "CDAL"

def test_user_password_hash_is_sha256_aigre(testapp):
    with testapp.app_context():
        user = User.query.get("CDAL")
        assert user is not None
        m = sha256(); m.update("AIGRE".encode())
        assert user.Password == m.hexdigest()

def test_load_user_existing(testapp):
    with testapp.app_context():
        user = load_user("CDAL")
        assert user is not None
        assert user.Login == "CDAL"

def test_load_user_unknown_returns_none(testapp):
    with testapp.app_context():
        assert load_user("unknown") is None
