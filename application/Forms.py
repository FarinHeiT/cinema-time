from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class Create_Room_Form(FlaskForm):
    room_name = StringField(validators=[DataRequired()])
    private_room = BooleanField()
    room_password = StringField()
    create_room = SubmitField()
    link = SubmitField()




class Chat_form(FlaskForm):
    message = StringField(validators=[DataRequired()])
    send_message = SubmitField()

