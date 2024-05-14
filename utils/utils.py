from typing import Any

from loguru import logger
from dotenv import find_dotenv, load_dotenv


def log_request(response: Any, *args: Any, **kwargs: Any) -> None:
    """
    Logs the request URL, headers, and body.

    Args:
        response: The response object containing request information.
        *args: Additional arguments (unused in this function).
        **kwargs: Additional keyword arguments (unused in this function).
    """

    logger.debug(f"Request: {response.request.method} {response.request.url}")
    logger.debug(f"Headers: {response.request.headers}")
    logger.debug(f"Body: {response.request.body}")


def log_response(response: Any, *args: Any, **kwargs: Any) -> None:
    """
    Logs the response status code, headers, and body.

    Args:
        response: The response object containing response information.
        *args: Additional arguments (unused in this function).
        **kwargs: Additional keyword arguments (unused in this function).
    """

    logger.debug(f"Response Status Code: {response.status_code}")
    logger.debug(f"Response Headers: {response.headers}")
    logger.debug(f"Response Body: {response.text}")

