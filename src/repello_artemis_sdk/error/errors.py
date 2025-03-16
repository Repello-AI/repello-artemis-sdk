from requests.exceptions import RequestException


class ArtemisApiError(RequestException):
    pass
