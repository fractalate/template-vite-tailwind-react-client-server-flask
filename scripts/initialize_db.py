from database.models import db
from app import create_app

def danger_drop_db(app):
    if app.config['TESTING'] is not True:
        raise RuntimeError('Refusing to drop database when not testing.')
    with app.app_context():
        db.drop_all()

def initialize_db(app):
    with app.app_context():
        db.create_all()
    print('Database initialized!')

if __name__ == '__main__':
    app = create_app()
    initialize_db(app)
