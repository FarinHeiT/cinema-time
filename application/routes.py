from flask import Blueprint, render_template
from .Forms import Create_Room_Form

general = Blueprint('general', __name__)


@general.route('/')
def index():
    form = Create_Room_Form()
    return render_template('index.html', form=form)

