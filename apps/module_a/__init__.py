from flask import Blueprint
from . import view


def register_url():
    bp = Blueprint('module_a', __name__, url_prefix='/module_a')
    bp.add_url_rule('/a_a', view_func=view.a_a_view, endpoint='a_a', methods=('GET',))

    return bp
