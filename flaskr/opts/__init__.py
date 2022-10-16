from flask import Blueprint

opts = Blueprint('opts', __name__,  url_prefix='')

from . import routes
