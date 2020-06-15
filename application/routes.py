from flask import Blueprint, Response

general = Blueprint('general', __name__)


@general.route('/')
def index():
    return Response('<h1>HEY</h1>')
