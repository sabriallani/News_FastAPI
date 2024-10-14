from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()

# Configuration de Jinja2 pour le rendu des templates
templates = Jinja2Templates(directory="templates")

# Clé API et URL de l'API de News (NewsAPI)
NEWS_API_KEY = "c464de31d4234bbbb5e10a28ab7d643d"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

@app.get("/", response_class=HTMLResponse)
async def get_news(request: Request):
    # Paramètres pour l'appel à l'API (nouvelles de la France)
    params = {
        'country': 'us',
        'apiKey': NEWS_API_KEY
    }

    # Appel API pour obtenir les actualités
    async with httpx.AsyncClient() as client:
        response = await client.get(NEWS_API_URL, params=params)
        news_data = response.json()

    # Vérifie que la réponse contient bien des articles
    if "articles" in news_data:
        articles = news_data["articles"]
    else:
        articles = []

    # Affiche les données dans les logs pour débogage
    print(news_data)

    # Rendre le template avec les données des articles
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles})
