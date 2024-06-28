from config import configs
from database.models import db
from flask import Flask
from routes.api import api_bp

import os

def determine_config_name() -> str:
    config_name = os.getenv('PYTHON_ENV')
    if config_name is None:
        return 'development'
    return config_name

def create_app(config_name = None) -> Flask:
    if config_name is None:
        config_name = determine_config_name()

    app = Flask(__name__)
    print('Creating app with config ' + config_name)
    app.config.from_object(configs[config_name])

    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
