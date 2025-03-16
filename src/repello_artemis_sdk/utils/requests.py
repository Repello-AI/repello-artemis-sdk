import requests

from ..error import ArtemisApiError


class ArtemisHttpClient:
    """
    ArtemisHttpClient is a class that is used to make HTTP requests to the Artemis API.
    """

    TIMEOUT = 30

    def __init__(self, client_id: str, api_key: str):
        self.client_id = client_id
        self.api_key = api_key
        self.default_headers = {
            "X-Client-ID": self.client_id,
            "X-Client-Secret": self.api_key,
            "Content-Type": "application/json",
        }

    def get(
        self, url: str, params: dict | None = None, headers: dict | None = None
    ) -> requests.Response:
        """
        Send a GET request to the specified url.

        :param url: The url to send the request to
        :param params: The query parameters to include in the request
        :param headers: Additional headers to merge with default headers
        :return: The response from the server
        """

        try:
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)

            response = requests.get(
                url, headers=request_headers, params=params, timeout=self.TIMEOUT
            )
            return response
        except requests.RequestException as e:
            raise ArtemisApiError(e)

    def post(
        self, url: str, data: dict | None = None, headers: dict | None = None
    ) -> requests.Response:
        """
        Send a POST request to the specified url.

        :param url: The url to send the request to
        :param data: The JSON data to include in the request body
        :param headers: Additional headers to merge with default headers
        :return: The response from the server
        """
        try:
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)

            response = requests.post(
                url, headers=request_headers, json=data, timeout=self.TIMEOUT
            )
            return response
        except requests.RequestException as e:
            raise ArtemisApiError(e)

    def put(
        self, url: str, data: dict | None = None, headers: dict | None = None
    ) -> requests.Response:
        """
        Send a PUT request to the specified url.

        :param url: The url to send the request to
        :param data: The JSON data to include in the request body
        :param headers: Additional headers to merge with default headers
        :return: The response from the server
        """
        try:
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)

            response = requests.put(
                url, headers=request_headers, json=data, timeout=self.TIMEOUT
            )
            return response
        except requests.RequestException as e:
            raise ArtemisApiError(e)

    def delete(
        self, url: str, params: dict | None = None, headers: dict | None = None
    ) -> requests.Response:
        """
        Send a DELETE request to the specified url.

        :param url: The url to send the request to
        :param params: The query parameters to include in the request
        :param headers: Additional headers to merge with default headers
        :return: The response from the server
        """
        try:
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)

            response = requests.delete(
                url, headers=request_headers, params=params, timeout=self.TIMEOUT
            )
            return response
        except requests.RequestException as e:
            raise ArtemisApiError(e)

    def patch(
        self, url: str, data: dict | None = None, headers: dict | None = None
    ) -> requests.Response:
        """
        Send a PATCH request to the specified url.

        :param url: The url to send the request to
        :param data: The JSON data to include in the request body
        :param headers: Additional headers to merge with default headers
        :return: The response from the server
        """
        try:
            request_headers = self.default_headers.copy()
            if headers:
                request_headers.update(headers)

            response = requests.patch(
                url, headers=request_headers, json=data, timeout=self.TIMEOUT
            )
            return response
        except requests.RequestException as e:
            raise ArtemisApiError(e)
