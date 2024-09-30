from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import main
from ..models import db, Speaker

@main.route('/add_speaker', methods=['GET', 'POST'])
@login_required
def add_speaker():
    if request.method == 'POST':
        name = request.form['name']
        new_speaker = Speaker(name=name)
        db.session.add(new_speaker)
        db.session.commit()
        flash('Speaker added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_speaker.html')
