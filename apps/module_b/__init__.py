from flask import Blueprint
from . import view


def register_url():
    bp = Blueprint('module_b', __name__, url_prefix='/module_b')
    bp.add_url_rule('/b_b', view_func=view.b_b_view, endpoint='b_b', methods=('GET',))

    return bp
