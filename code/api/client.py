import time
from http import HTTPStatus

import requests
from flask import current_app
from requests.exceptions import ConnectionError, SSLError

from api.utils import request_body, BearerAuth, result_request_body, add_error
from api.errors import (
    AuthorizationError,
    LogRhythmSSLError,
    LogRhythmConnectionError,
    MoreMessagesAvailableWarning,
)

INVALID_CREDENTIALS = 'wrong access_id or access_key'


SEARCH_STATUSES = (
    'Searching',
    'First Results',
)


class LogRhythmClient:
    def __init__(self, credentials):
        self._credentials = credentials
        self._headers = {
            'User-Agent': current_app.config['USER_AGENT']
        }
        self._entities_limit = current_app.config['CTR_ENTITIES_LIMIT']
        self._default_entities_limit = \
            current_app.config['CTR_DEFAULT_ENTITIES_LIMIT']

    @property
    def _url(self):
        url = current_app.config['LOGRHYTHM_API_ENDPOINT']
        return url.format(host=self._credentials.get('host'))

    def health(self):
        payload = request_body(current_app.config.get('HEALTH_IP'), 9)
        return self._request(path='search-task', payload=payload)

    def _get_search_task_id(self, observable):
        payload = request_body(observable.get('value'), 4)
        task_id = ''
        response = self._request(path='search-task', payload=payload)
        if response:
            task_id = response.get('TaskId')
        return task_id

    def get_data(self, observable):
        path = 'search-result'
        max_retry_count = 10
        check_request_delay = 5
        search_limit = 101
        items = []
        task_id = self._get_search_task_id(observable)

        if task_id:
            payload = result_request_body(task_id)
            response = self._request(path=path, payload=payload)

            while (response.get('TaskStatus') in SEARCH_STATUSES and
                   len(response.get('Items')) < search_limit and
                   max_retry_count):
                time.sleep(check_request_delay)
                max_retry_count -= 1
                response = self._request(path=path, payload=payload)

            if (len(response.get('Items')) == search_limit and
                    self._entities_limit == self._default_entities_limit):
                add_error(MoreMessagesAvailableWarning(observable))

            items = response.get('Items')[:self._entities_limit]

        return items

    def _request(self, path, method='POST', payload=None, params=None):
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
        elif response.status_code == HTTPStatus.BAD_REQUEST:
            return {}
