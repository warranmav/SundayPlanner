from flask import redirect, url_for, flash
from flask_login import login_required
from . import main
from ..models import db, Speaker

@main.route('/delete_speaker/<int:id>', methods=['POST'])
@login_required
def delete_speaker(id):
    speaker = Speaker.query.get_or_404(id)
    db.session.delete(speaker)
    db.session.commit()
    flash('Speaker deleted successfully!')
    return redirect(url_for('main.index'))
