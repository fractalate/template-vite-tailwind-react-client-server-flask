from flask import Blueprint, abort, request
from database.models import db, Widget

import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/test/ping', methods=['GET'])
def get_ping():
    return json.dumps({
        'message': 'pong',
    })

@api_bp.route('/test/pg', methods=['GET'])
def get_test_postgres():
    result = Widget.query.all()
    return json.dumps({
        'data': result,
    })
