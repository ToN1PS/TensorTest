import time
from functools import wraps

from typing import Callable, Any


def redirect_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(self, *arg, **kwargs) -> None:
        time.sleep(3.0)
        result = func(self)
        time.sleep(3.0)
        return result

    return wrapper
