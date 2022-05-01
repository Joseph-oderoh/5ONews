from flask import render_template
from app import app
from .request import get_source


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    source= get_source()
    return render_template('index.html',sources=source,)

@app.route('/article/<int:article_id>')
def article(article_id):
    return render_template('article.html',id = article_id)