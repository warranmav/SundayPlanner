from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import main
from ..models import db, Speaker

@main.route('/update_speaker/<int:id>', methods=['GET', 'POST'])
@login_required
def update_speaker(id):
    speaker = Speaker.query.get_or_404(id)
    if request.method == 'POST':
        speaker.name = request.form['name']
        speaker.topic = request.form['topic']
        db.session.commit()
        flash('Speaker updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('update_speaker.html', speaker=speaker)
