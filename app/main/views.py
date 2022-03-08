from turtle import title
from flask import render_template
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Elevator Pitch'
    return render_template('index.html', title = title)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):