from unicodedata import category
from app import app
import urllib.request,json
from .models import article
#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_ARTICAL_BASE_URL']
def get_articles(article):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response =json.loads(get_articles_data)
        article_results = None

        if get_articles_response['results']:
           article_results_list = get_articles_response['results']
           article_results = process_results(article_results_list)


    return article_results
def process_results(article_list):
    movie_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        overview = article_item.get('description')
        poster = article_item.get('poster_path')
        vote_average = article_item.get('vote_average')
        vote_count = article_item.get('vote_count')

        if poster:
            article_object = article(source,author,title,overview,poster,vote_average,vote_count)
            article_results.append(article_object)

    return article_results