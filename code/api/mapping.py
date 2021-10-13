from datetime import datetime, timezone

from api.utils import transient_id


CTIM_DEFAULTS = {
    'schema_version': '1.1.8',
}

TITLE = SHORT_DESCRIPTION = \
    'A LogRhythm event in last 30 days contains observable'

SIGHTING = 'sighting'

SIGHTING_DEFAULTS = {
    'count': 1,
    'internal': True,
    'confidence': 'High',
    'type': SIGHTING,
    'source': 'LogRhythm',
    'title': TITLE,
    'short_description': SHORT_DESCRIPTION,
}


class Sighting:
    def __init__(self, observable):
        self.observable = observable

    @staticmethod
    def _time_format(time: int) -> str:
        return datetime.fromtimestamp(
            time / 1000.0,
            timezone.utc).isoformat(timespec='milliseconds')

    def _observed_time(self, time: int) -> dict:
        return {
            'start_time': self._time_format(time),
        }

    @staticmethod
    def _make_sighting_data_table(log_info: dict) -> dict:
        data = {'columns': [], 'rows': [[]]}

        for key, value in log_info.items():
            data['columns'].append({'name': key, 'type': 'string'})
            data['rows'][0].append(str(value))

        return data

    def extract(self, log_info: dict) -> dict:
        sighting = {
            'id': transient_id(SIGHTING),
            'data': self._make_sighting_data_table(log_info),
            'observed_time': self._observed_time(log_info.get('logDate')),
            'observables': [self.observable],
            **CTIM_DEFAULTS,
            **SIGHTING_DEFAULTS,
        }

        return sighting
