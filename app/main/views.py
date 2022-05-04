from flask import render_template,request,redirect,url_for

import app 
from . import main
from app.request import get_article_sources, get_articles, search_article
# from .forms import ReviewForm
# from ..models import Article




@main.route('/')
def index():

    top_headlines = get_articles()
    
    

    


    title = 'Hello! Welcome to the best News Site'


    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', article=search_article))
    else:

        return render_template('index.html', title=title, headlines=top_headlines)


@main.route('/search/<article>')
def search(article):

    article_name_list = article.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article}'
    return render_template('search.html', articles=searched_articles )

@main.route('/source')
def source():

    sources = get_article_sources()

    return render_template('source.html',  sources=sources)