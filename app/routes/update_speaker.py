from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from . import main
from ..models import db, Speaker, SpeakerException
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField
from wtforms.validators import DataRequired, Optional

# Define the form using Flask-WTF
class UpdateSpeakerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    exception_reason = SelectField('Exception Reason', choices=[
        ('Health Reasons', 'Health Reasons'),
        ('Refusal', 'Refusal'),
        ('Vacation', 'Vacation')
    ])
    expiry_date = DateField('Vacation Expiry Date', format='%Y-%m-%d', validators=[Optional()])

@main.route('/update_speaker/<int:speaker_id>', methods=['GET', 'POST'])
@login_required
def update_speaker(speaker_id):
    speaker = Speaker.query.get_or_404(speaker_id)
    form = UpdateSpeakerForm()

    if form.validate_on_submit():
        try:
            # Update speaker's name
            speaker.name = form.name.data

            # Handle the exception reason
            exception_reason = form.exception_reason.data
            expiry_date = form.expiry_date.data if exception_reason == 'Vacation' else None

            # Check if the speaker already has an exception
            speaker_exception = SpeakerException.query.filter_by(speaker_id=speaker.id).first()

            if speaker_exception:
                # Update the existing exception
                speaker_exception.reason = exception_reason
                speaker_exception.expiry_date = expiry_date
            else:
                # Create a new exception if none exists
                new_exception = SpeakerException(
                    speaker_id=speaker.id,
                    reason=exception_reason,
                    expiry_date=expiry_date
                )
                db.session.add(new_exception)

            # Commit the changes to the database
            db.session.commit()
            flash('Speaker updated successfully!', 'success')
            return redirect(url_for('main.index'))

        except Exception as e:
            db.session.rollback()  # Roll back changes if there is an error
            flash(f'An error occurred: {str(e)}', 'danger')

    # Prepopulate the form with the current speaker's data for the GET request
    form.name.data = speaker.name
    speaker_exception = SpeakerException.query.filter_by(speaker_id=speaker.id).first()
    if speaker_exception:
        form.exception_reason.data = speaker_exception.reason
        if speaker_exception.expiry_date:
            form.expiry_date.data = speaker_exception.expiry_date

    return render_template('update_speaker.html', speaker=speaker, form=form)
