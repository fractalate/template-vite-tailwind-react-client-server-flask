from config import configs
from flask import Flask
import os

def determine_config_name():
    config_name = os.getenv('PYTHON_ENV')
    if config_name is None:
        return 'development'
    return config_name

def create_app(config_name):
    app = Flask(__name__)
    print('Creating app with config ' + config_name)
    app.config.from_object(configs[config_name])
    return app

if __name__ == '__main__':
    config_name = determine_config_name()
    app = create_app(config_name)
    app.run(debug=True)
