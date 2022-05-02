import urllib.request,json
from .models import Article
from app import models

Article = models.Article

# Getting api key
api_key = None
# Getting the base url
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['ARTICLE_API_KEY']
    base_url = app.config['ARTICLE_API_BASE_URL']