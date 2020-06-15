from flask import Flask, Response

# from flask_redis import FlaskRedis

# r = FlaskRedis()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    # r.init_app(app)

    from . import routes

    app.register_blueprint(routes.general)
    # app.register_blueprint(admin.admin_bp)

    return app
