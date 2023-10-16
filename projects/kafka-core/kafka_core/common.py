from typing import Any

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_SEVER = "localhost:9092"


def green(value: Any) -> str:
    return f"\033[1;32m{value}\033[00m"
