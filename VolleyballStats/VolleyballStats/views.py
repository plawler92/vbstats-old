"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from VolleyballStats import app
from VolleyballStats.common import get_stats

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/', methods=['GET', 'POST'])
@app.route('/stats', methods=['GET', 'POST'])
def stats():
    """Renders the stats page."""
    players = ["mexico", "stephanie"]
    stats = get_stats()

    if request.method == 'POST':
        print("here")
        #print(request.form['mexico-kills'])
        #print(request.form)
        #print(request.data)
        print(request)

    return render_template(
        'stats.html',
        players=players,
        stats=stats
    )
   