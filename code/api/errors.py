AUTH_ERROR = 'authorization error'
INVALID_ARGUMENT = 'invalid argument'
UNKNOWN = 'unknown'
CONNECTION_ERROR = 'connection error'


class TRFormattedError(Exception):
    def __init__(self, code, message, type_='fatal'):
        super().__init__()
        self.code = code or UNKNOWN
        self.message = message or 'Something went wrong.'
        self.type_ = type_

    @property
    def json(self):
        return {'type': self.type_,
                'code': self.code,
                'message': self.message}


class AuthorizationError(TRFormattedError):
    def __init__(self, message):
        super().__init__(
            AUTH_ERROR,
            f'Authorization failed: {message}'
        )


class InvalidArgumentError(TRFormattedError):
    def __init__(self, message):
        super().__init__(
            INVALID_ARGUMENT,
            str(message)
        )


class WatchdogError(TRFormattedError):
    def __init__(self):
        super().__init__(
            code='health check failed',
            message='Invalid Health Check'
        )


class LogRhythmSSLError(TRFormattedError):
    def __init__(self, error):
        message = getattr(
            error.args[0].reason.args[0], 'verify_message', ''
        ) or error.args[0].reason.args[0].args[0]

        super().__init__(
            UNKNOWN,
            f'Unable to verify SSL certificate: {message}'
        )


class LogRhythmConnectionError(TRFormattedError):
    def __init__(self, url):
        super().__init__(
            CONNECTION_ERROR,
            'Unable to connect to LogRhythm,'
            f' validate the configured API endpoint: {url}'
        )


class MoreMessagesAvailableWarning(TRFormattedError):
    def __init__(self, observable):
        super().__init__(
            'too-many-messages-warning',
            f'More events in LogRhythm for {observable.get("value")} that can'
            ' be rendered. Log in to the LogRhythm console to see all events',
            type_='warning',
        )
