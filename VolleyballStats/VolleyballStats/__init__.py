"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

import VolleyballStats.views
#import VolleyballStats.database
#import VolleyballStats.models