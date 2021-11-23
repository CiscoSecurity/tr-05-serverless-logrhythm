from functools import partial

from flask import Blueprint, g

from api.client import LogRhythmClient
from api.mapping import Sighting
from api.schemas import ObservableSchema
from api.utils import (
    get_json,
    get_credentials,
    filter_observables,
    jsonify_result
)

enrich_api = Blueprint('enrich', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    credentials = get_credentials()
    observables = filter_observables(get_observables())

    g.sightings = []
    client = LogRhythmClient(credentials)

    for observable in observables:
        events = client.get_data(observable)
        mapping = Sighting(observable)

        for event in events:
            sighting = mapping.extract(event)
            g.sightings.append(sighting)

    return jsonify_result()
