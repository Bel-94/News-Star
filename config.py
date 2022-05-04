import os
from sre_constants import CATEGORY

class Config:

    ARTICLE_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCES_API_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    SEARCH_API_URL = 'https://newsapi.org/v2/top-headlines?q={}&apiKey={}'
    ARTICLE_API_KEY = 'd40e824fa8a14c068897a2e4d48882dd'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


