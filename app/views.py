from flask import render_template
from app import app
from .request import get_artices


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_articles = get_articles('popular')
    print(popular_articles)
    title = 'Home - Welcome to the best News Highlight Website Online'
    return render_template('index.html', title = title)

 