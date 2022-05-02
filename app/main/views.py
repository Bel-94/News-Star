from flask import render_template,request,redirect,url_for

import app
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review




@main.route('/')
def index():

    title = 'Hello! Welcome to the best News Site'

    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)