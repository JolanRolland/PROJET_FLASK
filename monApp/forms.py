from decimal import ROUND_HALF_UP
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, HiddenField
from wtforms.validators import DataRequired
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