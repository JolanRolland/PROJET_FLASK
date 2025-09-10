from .app import db
class Auteur(db.Model):
    idA = db.Column( db.Integer, primary_key=True )
    Nom = db.Column( db.String(100) )
    def __init__(self, Nom):
        self.Nom = Nom


class Livre(db.Model):
    idL = db.Column(db.Integer, primary_key=True)   
    Prix = db.Column(db.Float)                          
    Titre = db.Column(db.String(255))                  
    Url = db.Column(db.String(255))          
    Img = db.Column(db.String(255))                

    def __init__(self, Titre, Prix, Url, Img):
        self.Titre = Titre
        self.Prix = Prix
        self.Url = Url
        self.Img = Img
