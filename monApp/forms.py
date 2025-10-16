from decimal import ROUND_HALF_UP
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, HiddenField
from wtforms.validators import DataRequired
from wtforms import PasswordField
from . models import User
from hashlib import sha256

class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])

class FormLivre(FlaskForm):
    idL = HiddenField('idL')
    Titre = StringField('Titre')  # mets-le en readonly dans le template si non modifiable
    AuteurId = HiddenField('AuteurId')

    Prix = DecimalField(
        'Prix',
        places=2,
        rounding=ROUND_HALF_UP,
        validators=[
            DataRequired()
        ]
    )

class LoginForm(FlaskForm):
    Login = StringField('Identifiant')
    Password = PasswordField('Mot de passe')
    next = HiddenField()
    
    def get_authenticated_user (self):
        unUser = User.query.get(self.Login.data)
        if unUser is None:
            return None
        m = sha256 ()
        m.update(self.Password.data.encode())
        passwd = m.hexdigest()
        return unUser if passwd == unUser.Password else None