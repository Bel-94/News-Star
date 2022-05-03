from flask import render_template,requests,redirect,url_for

import app 
from . import main
from ..requests import get_articles,get_article,search_article
from .forms import ReviewForm
from ..models import Article




@main.route('/')
def index():

    trending_articles = get_articles('trending')
    upcoming_article = get_articles('upcoming')
    available_article = get_articles('available')

    title = 'Hello! Welcome to the best News Site'


    search_article = requests.args.get('article_query')

    if search_article:
        return redirect(url_for('search', article_name=search_article))
    else:

        return render_template('index.html', title=title, trending=trending_articles, upcoming=upcoming_article, available=available_article)

@main.route('/article/<int:article_id>')
def article(article_id):

    article = get_article(article_id)
    title = f'{article.title}'

    return render_template('article.html', title=title, article=article )

@main.route('/search/<article_name>')
def search(article_name):

    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html', articles=searched_articles )

if __name__ == '__main__':
    app.run(debug=True)