# from turtle import title
import urllib.request,json
from .models import Article, Source
from app import models

Article = models.Article

# Getting api key
api_key = None
# Getting the base url
base_url = None

# Getting the source url
source_url = None

# Getting the category url
search_url = None

def configure_request(app):
    global api_key, base_url, source_url, category_url
    api_key = app.config['ARTICLE_API_KEY']
    base_url = app.config['ARTICLE_API_BASE_URL']
    source_url = app.config['SOURCES_API_URL']
    search_url = app.config['SEARCH_API_URL']


def get_articles():
    '''
    Function that gets the json response to the url request
    '''

    articles_url = base_url.format(api_key)

    with urllib.request.urlopen(articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        artical_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)


    return article_results

def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of movie objects
    '''

    article_results = []
    for article_item in article_list:
        source_name = article_item.get('source["name"]')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        if image:
            article_object = Article(source_name, author, title, description, url, image, date)
            article_results.append(article_object)

    return article_results

def get_article_sources():
    get_article_details = source_url.format(api_key)

    with urllib.request.urlopen(get_article_details) as url:
         article_details_data = url.read()
         article_details_response = json.loads(article_details_data)

         article_object = None
         if article_details_response['sources']:
             source_name = article_details_response['sources']
             source_results = process_source_results(source_name)
             

    return source_results


def process_source_results(sources):
    source_results = []

    for source in sources:
        id = source.get('id')
        name = source.get('name')
        url = source.get('url')

        source = Source(id,name,url)
        source_results.append(source)

    return source_results


def search_article(article):
    search_article_url = search_url.format(api_key, article)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)

    return search_article_results








