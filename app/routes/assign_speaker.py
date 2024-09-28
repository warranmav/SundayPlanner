from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from . import main
from ..models import db, Speaker, Assignment


@main.route('/assign_speaker', methods=['GET', 'POST'])
@login_required
def assign_speaker():
    if request.method == 'POST':
        speaker_id = request.form['speaker_id']
        date_str = request.form['date']
        duration = request.form['duration']
        order = request.form['order']

        # Convert date string to datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if date.weekday() != 6:  # Ensure the date is a Sunday
            flash('Assignment date must be a Sunday')
            return redirect(url_for('main.assign_speaker'))

        new_assignment = Assignment(speaker_id=speaker_id, date=date, duration=duration, order=int(order))
        db.session.add(new_assignment)
        db.session.commit()
        flash('Speaker assigned successfully!')
        return redirect(url_for('main.assignments'))

    speakers = Speaker.query.all()
    return render_template('assign_speaker.html', speakers=speakers)


@main.route('/assignments')
@login_required
def assignments():
    assignments = Assignment.query.order_by(Assignment.date, Assignment.order).all()
    return render_template('assignments.html', assignments=assignments)
