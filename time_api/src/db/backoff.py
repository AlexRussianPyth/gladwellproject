import logging
from functools import wraps
import time


logger = logging.getLogger(__name__)


def backoff(exceptions: tuple, min_sleep_time: float = 0.1, factor: float = 2, max_sleep_time: float = 20):
    """Retry call a function with delay.

    The function tries to call an argument function after delay if the argument
    function caused an exception."""

    def func_wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            retry = 1
            delay = min_sleep_time
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    logger.exception(f"Error in {str(func)}. Next try in {delay} seconds")
                    time.sleep(delay)
                    delay = min_sleep_time * (retry ** factor) if delay < max_sleep_time else max_sleep_time
                    retry += 1
        return inner
    return func_wrapper
