# 📚 Catalogue de livres — Flask

> Une application web pédagogique pour parcourir des livres et leurs auteurs, et gérer le catalogue après connexion.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Flask-3.1-111827?logo=flask&logoColor=white" alt="Flask 3.1">
  <img src="https://img.shields.io/badge/SQLite-base%20de%20donn%C3%A9es-3E82A0?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Pytest-tests-0A9EDC?logo=pytest&logoColor=white" alt="Pytest">
</p>

## Le projet en bref

Ce projet, réalisé dans le cadre de mon BUT Informatique, m'a permis de construire une application Flask de bout en bout : modèles de données, vues, formulaires, authentification, templates et tests.

| Côté visiteur | Après connexion |
| --- | --- |
| Consulter les listes et fiches des livres et auteurs | Créer, modifier et supprimer des auteurs |
| Accéder aux pages d'information | Modifier les fiches des livres |

Les données sont stockées dans **SQLite** avec **SQLAlchemy**. Chaque livre est lié à un auteur. Les formulaires utilisent **Flask-WTF**, et les opérations d'édition sont protégées par **Flask-Login**.

## Ce que j'ai travaillé

- Modélisation des entités `Livre`, `Auteur` et `User`, avec une relation entre livres et auteurs.
- Mise en place des routes Flask, des vues et des templates Jinja.
- Création des formulaires de consultation et d'édition, avec validation.
- Gestion des connexions et protection des pages d'édition.
- Tests unitaires et fonctionnels avec Pytest et mesure de couverture avec Coverage.

## Stack et structure

```text
monApp/
├── app.py          # Application Flask et extensions
├── models.py       # Modèles SQLAlchemy
├── views.py        # Routes et vues
├── forms.py        # Formulaires
├── commands.py     # Commandes de préparation de la base
├── templates/      # Pages Jinja
├── static/         # Ressources statiques
├── data/           # Données d'exemple
└── tests/          # Tests unitaires et fonctionnels
```

**Technologies :** Python · Flask · SQLAlchemy · SQLite · Flask-Login · Flask-WTF · Jinja · Bootstrap · Pytest.

## Lancer le projet

Prérequis : Python 3 et Git.

```bash
git clone https://github.com/JolanRolland/PROJET_FLASK.git
cd PROJET_FLASK
python -m venv .venv
```

Activez l'environnement virtuel :

- **Windows PowerShell :** `.venv\Scripts\Activate.ps1`
- **macOS / Linux :** `source .venv/bin/activate`

Installez les dépendances et préparez la base :

```bash
pip install -r requirements.txt
flask loaddb monApp/data/data.yml
flask syncdb
flask newuser demo mot-de-passe-local
flask run
```

Ouvrez ensuite l'adresse indiquée par Flask dans le terminal, généralement `http://127.0.0.1:5000`.

> **Attention :** `flask loaddb` supprime et recrée les tables avant d'importer les données d'exemple. Utilisez cette commande uniquement sur une base locale de démonstration.

## Tests

```bash
coverage run -m pytest
coverage report -m
```

Les tests couvrent les modèles, les formulaires et plusieurs parcours des livres et des auteurs. Le compte rendu du projet indique une couverture de **91 %** lors de la dernière mesure documentée.

---

Réalisé par [Jolan Rolland](https://github.com/JolanRolland) · [Me retrouver sur LinkedIn](https://www.linkedin.com/in/jolan-rolland-14982a389/)
