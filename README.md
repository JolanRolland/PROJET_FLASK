# PROJET FLASK

**Rolland Jolan**

---

## Lancer l'application
* Lancer l'environnement virtuel venv source venv/bin/activate
* Installer les dépendances : `pip install -r requirements.txt`
* Lancer application : `flask run`

---

## TP 1 

* Création de l'environnement virtuel.
* `pip freeze > requirements.txt`
* Ajout de la page About.
* Ajout de la page Contact.

---

## TP 2 

* Création du fichier `monApp.db`.
* Installation de `flask-sqlalchemy` et mise à jour de `requirements.txt`.
* Ajout du fichier `models.py`.
* Code de la classe `Livre`.
* Ajout de la relation **Many-to-One**.
* Ajout du fichier `commands.py`.
* Ajout du fichier `data.yml` et installation de `pyyaml`.
* Tests des commandes dans le shell Flask.

---

## TP 3 

* Ajout du template `index.html`.
* Création des templates `about.html` et `contact.html`.
* Liaison des templates dans `views.py`.

---

## TP 4

* Création du template `base.html`
* Modification du template `base.html` pour y ajouter une navbar que j'ai créé
* Utilisation du template `base.html` pour les fichiers `about.html` `contact.html` `index.html`
* Ajouts de paramètres pour la vue Index `base.html` 
* Création de la page `livres_list.html`
* Utilisation de bootstrap dans le template `base.html`

---

## TP 5

* Génération d'une nouvelle clé secrète avec la commande uuidgen `base.html`
Création des vues getAuteurById et updateAuteur
Création du template auteur_update.html

TP6
Création de User dans la bd models.py