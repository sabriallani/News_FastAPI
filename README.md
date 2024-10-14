
# API FastAPI pour Collecter et Afficher les Actualités

## Description

Ce projet implémente une API en utilisant **FastAPI** pour récupérer des actualités à partir d'une source externe (NewsAPI) et les afficher dans une page web en utilisant **Jinja2** pour le rendu HTML avec **Bootstrap** pour la mise en page.

## Fonctionnalités

1. **Récupérer les dernières actualités** : 
   - Endpoint : `GET /`
   - Permet de récupérer les dernières actualités d'un pays (par défaut : les États-Unis) à partir de l'API NewsAPI.

## Prérequis

- **Python 3.7+**
- **FastAPI**, **Uvicorn**, **httpx**, et **Jinja2** pour l'interface.

## Installation

1. **Cloner le projet :**

   ```bash
   git clone https://github.com/votre-repo/api-news.git
   cd api-news
   ```

2. **Créer un environnement virtuel et installer les dépendances :**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Pour Linux/Mac
   venv\Scripts\activate     # Pour Windows

   pip install fastapi uvicorn jinja2 httpx
   ```

3. **Clé API NewsAPI :**
   - Obtenez une clé API gratuite de [NewsAPI](https://newsapi.org/).
   - Remplacez la clé dans le fichier `main.py` à la ligne suivante :
     ```python
     NEWS_API_KEY = "votre_cle_api"
     ```

## Lancer le serveur FastAPI

1. **Exécution du serveur :**

   ```bash
   uvicorn main:app --reload
   ```

2. **Accéder à l'application :**
   - Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

## Explication du Code

### 1. Récupération des actualités depuis NewsAPI

Dans `main.py`, nous utilisons la bibliothèque **httpx** pour effectuer une requête asynchrone à l'API de NewsAPI afin de récupérer les dernières actualités.

Voici les paramètres utilisés pour l'appel API :
```python
params = {
    'country': 'us',  # Le pays dont nous voulons obtenir les actualités (par défaut : États-Unis)
    'apiKey': NEWS_API_KEY  # La clé API de NewsAPI
}
```

### 2. Rendu des actualités dans un template HTML

Nous utilisons **Jinja2** pour gérer le rendu des actualités dans un fichier HTML appelé `index.html` situé dans le dossier `templates`.

Chaque article récupéré contient les informations suivantes :
- Titre
- Description
- Lien vers l'article complet
- Image de l'article

### Exemple d'utilisation avec Postman ou cURL

#### a. Pour tester la récupération des actualités :

```bash
curl -X GET "http://127.0.0.1:8000/"
```

## Structure des fichiers

```
api-news/
│
├── main.py                 # Le fichier principal de l'API
├── templates/
│   └── index.html          # Le fichier HTML pour afficher les actualités
├── README.md               # Ce fichier
└── ...
```

## Fichier Template (index.html)

Voici un exemple de fichier `index.html` que vous pouvez placer dans le dossier `templates` pour afficher les actualités :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News API</title>
    <!-- Inclusion de Bootstrap -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4">Dernières Actualités</h1>
        <div class="row">
            {% for article in articles %}
            <div class="col-md-4">
                <div class="card mb-4">
                    <img src="{{ article['urlToImage'] }}" class="card-img-top" alt="Image" style="height: 200px; object-fit: cover;">
                    <div class="card-body">
                        <h5 class="card-title">{{ article['title'] }}</h5>
                        <p class="card-text">{{ article['description'] }}</p>
                        <a href="{{ article['url'] }}" class="btn btn-primary" target="_blank">Lire l'article</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    <!-- Inclusion des scripts Bootstrap -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

## Conclusion

Ce projet vous permet de récupérer et d'afficher des actualités en temps réel en utilisant une API externe (NewsAPI) et de rendre les informations sur une interface web élégante grâce à **Bootstrap**.
