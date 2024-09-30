from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .models import db, Speaker

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/add_speaker', methods=['GET', 'POST'])
@login_required
def add_speaker():
    if request.method == 'POST':
        name = request.form['name']
        new_speaker = Speaker(name=name)
        db.session.add(new_speaker)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_speaker.html')
