from flask import Blueprint

errors = Blueprint('errors', __name__, url_prefix='')

from . import handlers
