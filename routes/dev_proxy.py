from flask import Blueprint, Response, abort, request, jsonify

import os
import requests

dev_proxy_bp = Blueprint('dev_proxy', __name__)

VITE_DEV_PORT = os.getenv('VITE_DEV_PORT')

@dev_proxy_bp.route('/', defaults={ 'path': '' }, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@dev_proxy_bp.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def proxy(path):
    url = f"http://localhost:{VITE_DEV_PORT}/{request.path}"

    headers = {key: value for key, value in request.headers if key != 'Host'}

    method = request.method
    data = request.get_data()
    params = request.args

    resp = requests.request(method, url, headers=headers, data=data, params=params, cookies=request.cookies)

    response = Response(resp.content, status=resp.status_code)
    response.headers = {key: value for key, value in resp.headers.items() if key.lower() != 'content-encoding'}

    return response
