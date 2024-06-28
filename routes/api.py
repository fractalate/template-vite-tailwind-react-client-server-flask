from flask import Blueprint, abort, request
from database.models import db, Widget

import json

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
def get_test():
    return json.dumps({
        'message': 'Successful.',
    })

@api_bp.route('/test_database', methods=['GET'])
def get_test_database():
    result = Widget.query.all()
    return json.dumps({
        'data': result,
    })
