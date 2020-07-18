from flask import Blueprint, render_template
import json
from .Forms import Create_Room_Form
from . import redis_db

general = Blueprint('general', __name__)


@general.route('/', methods=('GET', 'POST'))
def index():
    form = Create_Room_Form()
    if form.validate_on_submit():
        '''RoomName : json{ users : { username : sid }, password : string, private : true/false, videos : { video : link }, host : sid  }'''
        roomname = form.room_name.data
        password = form.room_password.data
        private = form.private_room.data
        link = form.link.data
        redis_db.set(str(roomname), json.dumps({"password": password, "private": private, "videos": {"video": link}}))


    return render_template('index.html', form=form)

