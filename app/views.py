from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to the best News Highlight Website Online'
    return render_template('index.html', title = title)

 