from flask import render_template
from flask_login import login_required
from . import main
from ..models import Speaker, SpeakerException

@main.route('/speakers', methods=['GET'])
@login_required
def speakers():
    speakers = Speaker.query.all()
    speaker_exceptions = {exception.speaker_id: exception.reason for exception in SpeakerException.query.all()}
    return render_template('speakers.html', speakers=speakers, speaker_exceptions=speaker_exceptions)
