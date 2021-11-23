from flask import Blueprint

from api.client import LogRhythmClient
from api.utils import get_credentials, jsonify_data

health_api = Blueprint('health', __name__)


@health_api.route('/health', methods=['POST'])
def health():
    credentials = get_credentials()
    client = LogRhythmClient(credentials)
    _ = client.health()
    return jsonify_data({'status': 'ok'})
