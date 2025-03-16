import os
import logging
from .utils import ArtemisHttpClient, artemis_logger


class RepelloArtemisClient:
    """
    The client class for the Repello Artemis SDK.
    """

    def __init__(self, client_id: str, client_secret: str, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.http_client = ArtemisHttpClient(self.client_id, self.client_secret)

        self.logger = artemis_logger

        # Configure logging based on kwargs
        log_to_console = kwargs.get("log_to_console", False)
        log_to_file = kwargs.get("log_to_file", None)
        log_level = kwargs.get("log_level", logging.INFO)

        if log_to_console:
            self.enable_console_logging(level=log_level)

        if log_to_file:
            self.enable_file_logging(log_to_file, level=log_level)

    def enable_console_logging(self, level=logging.INFO):
        """
        Enable logging to console with the specified level and colored output.
        """

        from .utils import enable_console_logging

        enable_console_logging(level=level)

    def enable_file_logging(self, filepath, level=logging.DEBUG):
        """
        Enable logging to a file with the specified level.
        """

        from .utils import enable_file_logging

        enable_file_logging(filepath, level=level)

    @property
    def assets(self):
        """
        Access the assets API.
        """

        from .api import AssetApi

        return AssetApi(self.http_client)

    @property
    def users(self):
        """
        Access the users API.
        """

        from .api import UsersApi

        return UsersApi(self.http_client)

    @property
    def orgs(self):
        """
        Access the orgs API.
        """

        from .api import OrgsApi

        return OrgsApi(self.http_client)
