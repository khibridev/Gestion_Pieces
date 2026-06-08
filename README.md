# 🔧 Gestion des Pièces — Application Django

## Structure du projet
```
gestion_pieces/
├── gestion_pieces/       # Configuration Django
│   ├── settings.py
│   └── urls.py
├── pieces/               # Application principale
│   ├── models.py         # Modèles : Piece, MouvementStock
│   ├── views.py          # Vues de toutes les pages
│   ├── forms.py          # Formulaires
│   ├── urls.py           # Routes URL
│   └── admin.py
├── templates/pieces/     # Templates HTML
│   ├── base.html
│   ├── dashboard.html
│   ├── liste_pieces.html
│   ├── consommation.html
│   ├── reception.html
│   └── pieces_critiques.html
└── db.sqlite3            # Base de données SQLite
```

## Installation & Lancement

```bash
# 1. Installer Django
pip install django

# 2. Créer la base de données
python manage.py migrate

# 3. (Optionnel) Créer un admin
python manage.py createsuperuser

# 4. Lancer le serveur
python manage.py runserver
```

## Pages de l'application

| URL | Page |
|-----|------|
| `/` | Tableau de bord |
| `/pieces/` | Base de données des pièces |
| `/pieces/ajouter/` | Ajouter une pièce |
| `/consommation/` | Enregistrer une consommation |
| `/reception/` | Enregistrer une réception |
| `/critiques/` | Pièces critiques |
| `/admin/` | Interface d'administration |

## Fonctionnalités

- **Base de données** : CRUD complet sur les pièces avec filtres par type et recherche
- **Consommation** : Réduit automatiquement le stock + historique
- **Réception** : Augmente automatiquement le stock + historique
- **Pièces critiques** : Identifie automatiquement stock ≤ stock_minimum
- **Mouvements** : Historique complet de tous les mouvements (avant/après)
