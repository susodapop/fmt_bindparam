from flask import Blueprint

bp = Blueprint('fmt_bindparam', __name__, template_folder='templates')

from .routes import *