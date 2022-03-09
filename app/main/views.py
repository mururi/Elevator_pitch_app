from turtle import title
from unicodedata import category
from flask import render_template, request, redirect, url_for, abort, flash
from ..models import User, Pitch
from . import main
from flask_login import login_required, current_user
from .forms import UpdateProfile, NewPitch
from .. import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Elevator Pitch'
    pitches = Pitch.query.all()

    return render_template('index.html', title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches = user.pitches
    return render_template("profile/profile.html", user = user, pitches = pitches)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/new-pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = NewPitch()

    if form.validate_on_submit():
        category = form.category.data
        content = form.content.data
        author = current_user.id
        # downvotes = 0
        # upvotes = 0

        pitch = Pitch(category=category, content=content, author=author)

        db.session.add(pitch)
        db.session.commit()

        flash('Pitch Created', category = 'success')
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form = form)


# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):