from flask import Blueprint, render_template

room = Blueprint('room', __name__, url_prefix='/room')


@room.route('/<room_name>')
def room_details(room_name):
    return render_template('room.html')
