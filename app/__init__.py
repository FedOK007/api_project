import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    #import app.firstmodule.controllers as firstmodule

    #app.register_blueprint(firstmodule.module)

    @app.route('/')
    def index():
        return "Hello, World!"

    return app