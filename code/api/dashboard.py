from flask import Blueprint

from api.utils import jsonify_data, get_credentials, get_json
from api.schemas import DashboardTileSchema, DashboardTileDataSchema

dashboard_api = Blueprint('dashboard', __name__)


@dashboard_api.route('/tiles', methods=['POST'])
def tiles():
    _ = get_credentials()
    return jsonify_data([])


@dashboard_api.route('/tiles/tile', methods=['POST'])
def tile():
    _ = get_credentials()
    _ = get_json(DashboardTileSchema())
    return jsonify_data({})


@dashboard_api.route('/tiles/tile-data', methods=['POST'])
def tile_data():
    _ = get_credentials()
    _ = get_json(DashboardTileDataSchema())
    return jsonify_data({})
