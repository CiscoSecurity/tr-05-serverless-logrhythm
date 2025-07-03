from http import HTTPStatus
from unittest.mock import patch

from pytest import fixture

from tests.unit.conftest import mock_api_response
from tests.unit.api.utils import get_headers
from tests.unit.payloads_for_tests import (
    EXPECTED_RESPONSE_FROM_LOGRHYTHM,
    EXPECTED_RESPONSE_FROM_RELAY,
)


def routes():
    yield '/observe/observables'


def task_id():
    yield 'a4f34088-61f7-4331-97d4-4668736298b3'


def uuid4():
    yield '529b237b-b45a-41a4-9e68-197cdb0d6921'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


@fixture(scope='module')
def invalid_json_value():
    return [{'type': 'ip', 'value': ''}]


@patch('requests.get')
def test_enrich_call_with_valid_jwt_but_invalid_json_value(
        mock_request,
        route, client, valid_jwt, invalid_json_value,
        invalid_json_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=invalid_json_value)
    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_json_expected_payload(
        "{0: {'value': ['Field may not be blank.']}}"
    )


@fixture(scope='module')
def valid_json():
    return [{'type': 'ip', 'value': '10.0.15.255'}]


@patch('api.utils.uuid4')
@patch('api.client.LogRhythmClient._get_search_task_id')
@patch('requests.request')
@patch('requests.get')
def test_enrich_call_success(mock_get, mock_request, mock_task_id, mock_id,
                             route, client, valid_jwt, valid_json, test_keys_and_token):
    mock_get.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    mock_task_id.return_value = task_id()
    mock_request.return_value = mock_api_response(
        payload=EXPECTED_RESPONSE_FROM_LOGRHYTHM
    )
    mock_id.side_effect = uuid4()
    response = client.post(route, headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == EXPECTED_RESPONSE_FROM_RELAY


@patch('requests.request')
@patch('requests.get')
def test_enrich_call_with_unicode_encode_error(
        mock_get, mock_request, client, valid_jwt, valid_json, route,
        authorization_error_expected_relay_response, test_keys_and_token):

    mock_get.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    mock_request.side_effect = UnicodeEncodeError('codec', '\x00\x00',
                                                  1, 2, 'fake reason')

    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_error_expected_relay_response


@patch('requests.request')
@patch('requests.get')
def test_enrich_call_with_unauthorized_error(
        mock_get, mock_request, client, valid_jwt, valid_json, route,
        authorization_error_expected_relay_response, test_keys_and_token):

    mock_get.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    mock_request.return_value = mock_api_response(
        status_code=HTTPStatus.UNAUTHORIZED)

    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_error_expected_relay_response


@patch('requests.request')
@patch('requests.get')
def test_enrich_call_with_bad_request_error(
        mock_get, mock_request, client, valid_jwt, valid_json, route, test_keys_and_token):

    mock_get.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    mock_request.return_value = mock_api_response(
        status_code=HTTPStatus.BAD_REQUEST)

    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == {'data': {}}
