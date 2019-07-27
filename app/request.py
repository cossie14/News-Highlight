from app import app
from app import app
import urllib.request,json
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['e54ced74296d4e1f931fdc0e230e734c']
base_url = app.config["ARTICLE_API_BASE_URL"]def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)


    return article_results

