from flask import render_template
from app import app
from .request import get_articles


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_articles = get_articles('popular')
    print(trending_articles)(trending)
    title = 'Home - Welcome to the best News Highlight Website Online'
    return render_template('index.html',articles=article, trending = trending)


 