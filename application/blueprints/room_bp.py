from flask import Blueprint, render_template
from application import socketio

room = Blueprint('room', __name__, url_prefix='/room')


@room.route('/<room_name>', methods=('GET', 'POST'))
def room_details(room_name):
    return render_template('room.html')


@socketio.on('connect')
def handle_message():
    print('SMBD IS HERE!')