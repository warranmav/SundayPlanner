from flask import render_template
from flask_login import login_required
from . import main
from ..models import Speaker

@main.route('/speakers')
@login_required
def speakers():
    speakers = Speaker.query.all()
    return render_template('speakers.html', speakers=speakers)
