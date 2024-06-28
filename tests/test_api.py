from app import create_app
from scripts.initialize_db import danger_drop_db, initialize_db

import json
import pytest

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    with app.app_context():
        danger_drop_db(app)
        initialize_db(app)
    yield app

def test_api(client):
    rv = client.get('/api/test')
    assert rv.status_code == 200
    json.loads(rv.data)

def test_database(client):
    rv = client.get('/api/test_database')
    assert rv.status_code == 200
    json.loads(rv.data)
