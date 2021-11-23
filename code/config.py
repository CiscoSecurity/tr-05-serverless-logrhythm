import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings['VERSION']
    USER_AGENT = ('SecureX Threat Response Integrations '
                  '<tr-integrations-support@cisco.com>')
    CTR_DEFAULT_ENTITIES_LIMIT = 100

    LOGRHYTHM_API_ENDPOINT = 'https://{host}/lr-search-api/actions'
    HEALTH_IP = '192.0.2.1'

    SUPPORTED_TYPES = [
        'ip',
        'ipv6',
    ]
