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
