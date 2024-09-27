from flask import Blueprint

main = Blueprint('main', __name__)

from . import index, add_speaker, update_speaker, delete_speaker, speakers
