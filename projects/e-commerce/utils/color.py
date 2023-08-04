from typing import Any


def cyan(value: Any) -> str:
    return f"\033[1;36m{value}\033[00m"


def green(value: Any) -> str:
    return f"\033[1;32m{value}\033[00m"
