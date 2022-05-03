# from turtle import title
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


def get_articles(category):
    '''
    Function that gets the json response to the url request
    '''

    get_articles_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        movie_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
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
        source_name = article_item.get('source_name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('image')
        date = article_item.get('date')

        if image:
            article_object = Article(source_name, author, title, description, url, image, date)
            article_results.append(article_object)

    return article_results

def get_article(artical_id):
    get_article_details_url = base_url.format(artical_id, api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
         article_details_data = url.read()
         article_details_response = json.loads(article_details_data)

         article_object = None
         if article_details_response:
             artical_id = article_details_response.get('artical_id')
             author = article_details_response.get('author')
             title = article_details_response.get('title')
             description = article_details_response.get('description')
             image = article_details_response.get('image')
             date = article_details_response.get('date')

             article_object = Article(artical_id, author, title, description, image, date)

    return article_object


# def search_article(article_name):
#     search_article_url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'.format(api_key, article_name)
#     with urllib.request.urlopen(search_article_url) as url:
#         search_article_data = url.read()
#         search_article_response = json.loads(search_article_data)

#         search_article_results = None

#         if search_article_response['results']:
#             search_article_list = search_article_response['results']
#             search_article_results = process_results(search_article_list)

#     return search_article_results








