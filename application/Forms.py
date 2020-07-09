from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField

class Create_Room_Form(FlaskForm):
    room_name = StringField()
    private_room = BooleanField()
    room_password = StringField()
    create_room = SubmitField()


class Chat_form(FlaskForm):
    pass

