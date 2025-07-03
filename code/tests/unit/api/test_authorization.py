from http import HTTPStatus
from unittest.mock import patch

from pytest import fixture
from requests.exceptions import SSLError, ConnectionError, InvalidURL

from api.errors import AUTH_ERROR
from tests.unit.api.utils import get_headers
from tests.unit.conftest import mock_api_response
from api.utils import (
    WRONG_PAYLOAD_STRUCTURE,
    WRONG_KEY,
    WRONG_AUDIENCE,
    KID_NOT_FOUND,
    JWKS_HOST_MISSING,
    WRONG_JWKS_HOST,
)


def routes():
    yield '/health'
    yield '/observe/observables'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


@fixture(scope='module')
def wrong_jwt_structure():
    return 'wrong_jwt_structure'


@fixture(scope='module')
def authorization_errors_expected_payload(route):
    def _make_payload_message(message):
        payload = {
            'errors': [{
                'code': AUTH_ERROR,
                'message': f'Authorization failed: {message}',
                'type': 'fatal'}]

        }
        return payload

    return _make_payload_message


def test_call_with_authorization_header_failure(
        route, client,
        authorization_errors_expected_payload
):
    response = client.post(route)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Authorization header is missing'
    )


def test_call_with_wrong_authorization_type(
        route, client, valid_jwt,
        authorization_errors_expected_payload
):
    response = client.post(
        route, headers=get_headers(valid_jwt(), auth_type='wrong_type')
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong authorization type'
    )


def test_call_with_wrong_jwt_structure(
        route, client, wrong_jwt_structure,
        authorization_errors_expected_payload
):
    response = client.post(route, headers=get_headers(wrong_jwt_structure))

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong JWT structure'
    )


@patch('requests.get')
def test_call_with_jwt_encoded_by_wrong_key(
        mock_request, route,
        client, valid_jwt,
        authorization_errors_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    response = client.post(
        route,
        headers=get_headers(valid_jwt(private_key=test_keys_and_token["wrong_private_key"]))
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(WRONG_KEY)


@patch('requests.get')
def test_call_with_wrong_jwt_payload_structure(
        mock_request,
        route, client, valid_jwt,
        authorization_errors_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])
    response = \
        client.post(route,
                    headers=get_headers(valid_jwt(wrong_structure=True)))

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        WRONG_PAYLOAD_STRUCTURE
    )


@patch('requests.get')
def test_call_with_wrong_audience(
        mock_request, route, client, valid_jwt,
        authorization_errors_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])

    response = client.post(
        route,
        headers=get_headers(valid_jwt(aud='wrong_aud'))
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        WRONG_AUDIENCE
    )


@patch('requests.get')
def test_call_with_wrong_kid(
        mock_request, route, client, valid_jwt,
        authorization_errors_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])

    response = client.post(
        route,
        headers=get_headers(valid_jwt(kid='wrong_kid'))
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        KID_NOT_FOUND
    )


@patch('requests.get')
def test_call_with_missing_jwks_host(
        mock_request, route, client, valid_jwt,
        authorization_errors_expected_payload,
        test_keys_and_token
):
    mock_request.return_value = \
        mock_api_response(payload=test_keys_and_token["jwks"])

    response = client.post(
        route,
        headers=get_headers(valid_jwt(wrong_jwks_host=True))
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        JWKS_HOST_MISSING
    )


@patch('requests.get')
def test_call_with_wrong_jwks_host(
        mock_request, route, client, valid_jwt,
        authorization_errors_expected_payload):

    for error in (ConnectionError, InvalidURL):
        mock_request.side_effect = error()

        response = client.post(route, headers=get_headers(valid_jwt()))

        assert response.status_code == HTTPStatus.OK
        assert response.json == authorization_errors_expected_payload(
            WRONG_JWKS_HOST)


@patch('requests.request')
@patch('requests.get')
def test_call_with_ssl_error(mock_get, mock_request,
                             mock_exception_for_ssl_error,
                             client, valid_jwt,
                             ssl_error_expected_relay_response,
                             test_keys_and_token):

    mock_get.return_value = mock_api_response(
        payload=test_keys_and_token["jwks"]
    )
    mock_request.side_effect = SSLError(mock_exception_for_ssl_error)

    response = client.post('/health',
                           headers=get_headers(valid_jwt()))
    assert response.status_code == HTTPStatus.OK
    assert response.json == ssl_error_expected_relay_response


@patch('requests.request')
@patch('requests.get')
def test_call_with_connection_error(
        mock_get, mock_request,
        client, valid_jwt,
        connection_error_expected_relay_response,
        test_keys_and_token):

    mock_get.return_value = mock_api_response(
        payload=test_keys_and_token["jwks"]
    )
    mock_request.side_effect = ConnectionError()

    response = client.post('/health',
                           headers=get_headers(valid_jwt()))

    assert response.status_code == HTTPStatus.OK
    assert response.json == connection_error_expected_relay_response
