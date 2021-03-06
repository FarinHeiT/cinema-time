from flask import Flask, Response
from application import config
from flask_socketio import SocketIO
import redis

redis_db = redis.Redis(host='localhost', port=6379, db=0)

socketio = SocketIO()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config)

    socketio.init_app(app)

    from . import routes
    from application.blueprints import room_bp

    app.register_blueprint(routes.general)
    app.register_blueprint(room_bp.room)
    # app.register_blueprint(admin.admin_bp)

    return app
