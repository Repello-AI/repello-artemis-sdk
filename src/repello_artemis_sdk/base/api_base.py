from ..utils import ArtemisHttpClient


class BaseApi:
    """
    Base class for all API classes
    """

    def __init__(self, artemis_client: ArtemisHttpClient):
        self.api_client = artemis_client
