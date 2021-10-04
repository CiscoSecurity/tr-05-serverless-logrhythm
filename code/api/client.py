from http import HTTPStatus

import requests
from flask import current_app
from requests.exceptions import ConnectionError, SSLError

from api.utils import request_body, BearerAuth
from api.errors import (
    AuthorizationError,
    LogRhythmSSLError,
    LogRhythmConnectionError,
)

INVALID_CREDENTIALS = 'wrong access_id or access_key'


class LogRhythmClient:
    def __init__(self, credentials):
        self._credentials = credentials
        self._headers = {
            'User-Agent': current_app.config['USER_AGENT']
        }

    @property
    def _url(self):
        url = current_app.config['LOGRHYTHM_API_ENDPOINT']
        return url.format(host=self._credentials.get('host'))

    def health(self):
        payload = request_body(current_app.config.get('HEALTH_IP'), 9)
        return self._request(path='search-task', payload=payload,
                             method='POST')

    def _request(self, path, method='GET', payload=None, params=None):
        url = '/'.join([self._url, path.lstrip('/')])

        try:
            response = requests.request(method, url, json=payload,
                                        params=params,
                                        headers=self._headers,
                                        auth=BearerAuth(
                                            self._credentials['token']
                                        ))
        except SSLError as error:
            raise LogRhythmSSLError(error)
        except UnicodeEncodeError:
            raise AuthorizationError(INVALID_CREDENTIALS)
        except ConnectionError:
            raise LogRhythmConnectionError(self._url)

        if response.ok:
            return response.json()
        elif response.status_code == HTTPStatus.UNAUTHORIZED:
            raise AuthorizationError(INVALID_CREDENTIALS)
