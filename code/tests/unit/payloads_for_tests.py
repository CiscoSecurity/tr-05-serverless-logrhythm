EXPECTED_RESPONSE_OF_JWKS_ENDPOINT = {
    'keys': [
        {
            'kty': 'RSA',
            'n': 'tSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
                 'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
                 'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
                 '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
                 'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
                 '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
                 'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
                 'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
                 'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
                 'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
                 'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
                 '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
                 'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
                 'k3jNdVM',
            'e': 'AQAB',
            'alg': 'RS256',
            'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            'use': 'sig'
        }
    ]
}

RESPONSE_OF_JWKS_ENDPOINT_WITH_WRONG_KEY = {
    'keys': [
        {
            'kty': 'RSA',
            'n': 'pSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V'
                 'mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H'
                 'vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17'
                 '_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB'
                 'Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7'
                 '33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke'
                 'Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2'
                 'Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8'
                 'uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M'
                 'loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU'
                 'jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM'
                 '-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35'
                 'YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR'
                 'k3jNdVM',
            'e': 'AQAB',
            'alg': 'RS256',
            'kid': '02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            'use': 'sig'
        }
    ]
}

PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''

EXPECTED_RESPONSE_FROM_LOGRHYTHM_SEARCH_TASK = {
    'StatusCode': 200,
    'StatusMessage': 'Success',
    'ResponseMessage': 'Success',
    'TaskStatus': 'Searching',
    'TaskId': 'a4f34088-61f7-4331-97d4-4668736298b3'
}


EXPECTED_RESPONSE_FROM_LOGRHYTHM = {
    'StatusCode': 200,
    'StatusMessage': 'Success',
    'ResponseMessage': 'Success',
    'TaskStatus': 'Search Failed',
    'FilteredLogsCount': 101,
    'AllLogsCount': 101,
    'Items': [
        {
            'keyField': 'messageId',
            'count': 1,
            'classificationId': 3200,
            'classificationName': 'Error',
            'classificationTypeName': 'Operations',
            'commonEventName': 'No Translation Group Found For Protocol',
            'commonEventId': 6788,
            'direction': 2,
            'directionName': 'Internal',
            'entityId': 1,
            'entityName': 'Primary Site',
            'rootEntityId': 1,
            'rootEntityName': 'Primary Site',
            'impactedEntityId': 1,
            'impactedEntityName': 'Primary Site',
            'impactedHost': '10.0.15.255',
            'impactedIp': '10.0.15.255',
            'impactedPort': 138,
            'impactedZoneName': 'Internal',
            'indexedDate': 1633691826597,
            'insertedDate': 1632167822037,
            'logDate': 1632142608463,
            'logSourceHost': '192.168.78.155',
            'logSourceHostId': 2,
            'logSourceHostName': '192.168.78.155',
            'logSourceId': 10,
            'logSourceName': '192.168.78.155 Cisco ASA',
            'logSourceType': 162,
            'logSourceTypeName': 'Syslog - Cisco ASA',
            'messageId': '48810',
            'messageTypeEnum': 2,
            'mpeRuleId': 27239,
            'mpeRuleName': 'PIX-X-305005: No Translation Group Found',
            'normalDate': 1632167808477,
            'normalDateMin': 1632167808477,
            'normalMsgDateMax': 1632167808477,
            'normalDateHour': 1632164400000,
            'originEntityId': 1,
            'originEntityName': 'Primary Site',
            'originHostId': -1,
            'originHost': '10.0.15.77',
            'originIp': '10.0.15.77',
            'originPort': 138,
            'originZone': 0,
            'originZoneName': 'Internal',
            'priority': 44,
            'protocolId': 17,
            'protocolName': 'UDP',
            'portProtocol': '138/UDP',
            'severity': '3',
            'vendorMessageId': '305005'
        }
    ]
}

EXPECTED_RESPONSE_FROM_RELAY = {
    'data': {
        'sightings': {
            'count': 1,
            'docs': [
                {
                    'confidence': 'High',
                    'count': 1,
                    'data': {
                        'columns': [
                            {'name': 'keyField', 'type': 'string'},
                            {'name': 'count', 'type': 'string'},
                            {'name': 'classificationId', 'type': 'string'},
                            {'name': 'classificationName', 'type': 'string'},
                            {'name': 'classificationTypeName',
                             'type': 'string'},
                            {'name': 'commonEventName', 'type': 'string'},
                            {'name': 'commonEventId', 'type': 'string'},
                            {'name': 'direction', 'type': 'string'},
                            {'name': 'directionName', 'type': 'string'},
                            {'name': 'entityId', 'type': 'string'},
                            {'name': 'entityName', 'type': 'string'},
                            {'name': 'rootEntityId', 'type': 'string'},
                            {'name': 'rootEntityName', 'type': 'string'},
                            {'name': 'impactedEntityId', 'type': 'string'},
                            {'name': 'impactedEntityName', 'type': 'string'},
                            {'name': 'impactedHost', 'type': 'string'},
                            {'name': 'impactedIp', 'type': 'string'},
                            {'name': 'impactedPort', 'type': 'string'},
                            {'name': 'impactedZoneName', 'type': 'string'},
                            {'name': 'indexedDate', 'type': 'string'},
                            {'name': 'insertedDate', 'type': 'string'},
                            {'name': 'logDate', 'type': 'string'},
                            {'name': 'logSourceHost', 'type': 'string'},
                            {'name': 'logSourceHostId', 'type': 'string'},
                            {'name': 'logSourceHostName', 'type': 'string'},
                            {'name': 'logSourceId', 'type': 'string'},
                            {'name': 'logSourceName', 'type': 'string'},
                            {'name': 'logSourceType', 'type': 'string'},
                            {'name': 'logSourceTypeName', 'type': 'string'},
                            {'name': 'messageId', 'type': 'string'},
                            {'name': 'messageTypeEnum', 'type': 'string'},
                            {'name': 'mpeRuleId', 'type': 'string'},
                            {'name': 'mpeRuleName', 'type': 'string'},
                            {'name': 'normalDate', 'type': 'string'},
                            {'name': 'normalDateMin', 'type': 'string'},
                            {'name': 'normalMsgDateMax', 'type': 'string'},
                            {'name': 'normalDateHour', 'type': 'string'},
                            {'name': 'originEntityId', 'type': 'string'},
                            {'name': 'originEntityName', 'type': 'string'},
                            {'name': 'originHostId', 'type': 'string'},
                            {'name': 'originHost', 'type': 'string'},
                            {'name': 'originIp', 'type': 'string'},
                            {'name': 'originPort', 'type': 'string'},
                            {'name': 'originZone', 'type': 'string'},
                            {'name': 'originZoneName', 'type': 'string'},
                            {'name': 'priority', 'type': 'string'},
                            {'name': 'protocolId', 'type': 'string'},
                            {'name': 'protocolName', 'type': 'string'},
                            {'name': 'portProtocol', 'type': 'string'},
                            {'name': 'severity', 'type': 'string'},
                            {'name': 'vendorMessageId', 'type': 'string'}
                        ],
                        'rows': [
                            ['messageId', '1', '3200', 'Error', 'Operations',
                             'No Translation Group Found For Protocol',
                             '6788', '2', 'Internal', '1', 'Primary Site',
                             '1', 'Primary Site', '1', 'Primary Site',
                             '10.0.15.255', '10.0.15.255', '138', 'Internal',
                             '1633691826597', '1632167822037',
                             '1632142608463', '192.168.78.155', '2',
                             '192.168.78.155', '10',
                             '192.168.78.155 Cisco ASA', '162',
                             'Syslog - Cisco ASA', '48810', '2', '27239',
                             'PIX-X-305005: No Translation Group Found',
                             '1632167808477', '1632167808477',
                             '1632167808477', '1632164400000', '1',
                             'Primary Site', '-1', '10.0.15.77', '10.0.15.77',
                             '138', '0', 'Internal', '44', '17', 'UDP',
                             '138/UDP', '3', '305005'
                             ]
                        ]
                    },
                    'id': 'transient:sighting-529b237b-b45a-41a4-9e68-197cdb0'
                          'd6921',
                    'internal': True,
                    'observables': [{'type': 'ip', 'value': '10.0.15.255'}],
                    'observed_time': {
                        'start_time': '2021-09-20T12:56:48.463+00:00'
                    },
                    'schema_version': '1.1.8',
                    'short_description':
                        'A LogRhythm event in last 30 '
                        'days contains observable',
                    'source': 'LogRhythm',
                    'title':
                        'A LogRhythm event in last '
                        '30 days contains observable',
                    'type': 'sighting'
                }
            ]
        }
    }
}
