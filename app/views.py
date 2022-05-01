from app import app
from flask import render_template
from .request import article_source, get_headlines, get_source


# Views
@app.route('/')
def HOME():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    source= get_source()
    headlines = get_headlines()
    return render_template('index.html',sources=source,  headlines = headlines)


@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )
