from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Speaker

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_speaker', methods=['GET', 'POST'])
def add_speaker():
    if request.method == 'POST':
        name = request.form['name']
        topic = request.form['topic']
        new_speaker = Speaker(name=name, topic=topic)
        db.session.add(new_speaker)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_speaker.html')
