from flask import Blueprint

charts = Blueprint('charts', __name__,  url_prefix='')

from . import routes
