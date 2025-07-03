from http import HTTPStatus
from unittest.mock import patch

from pytest import fixture

from tests.unit.api.utils import get_headers
from tests.unit.conftest import mock_api_response


def routes():
    yield '/health'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


@patch('requests.request')
@patch('requests.get')
def test_health_call_success(mock_get, mock_request, route, client, valid_jwt, test_keys_and_token):
    mock_get.return_value = mock_api_response(
        payload=test_keys_and_token["jwks"]
    )
    mock_request.return_value = mock_api_response()
    response = client.post(route, headers=get_headers(valid_jwt()))
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'data': {'status': 'ok'}}
