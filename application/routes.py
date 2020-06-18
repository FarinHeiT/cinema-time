from flask import Blueprint, Response
from . import redis_db

general = Blueprint('general', __name__)


@general.route('/')
def index():
    return Response(redis_db.get("lol"))
