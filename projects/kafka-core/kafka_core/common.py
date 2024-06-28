from os import environ
from typing import Any

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_SEVER = environ.get("APP_KAFKA_HOST", "localhost:9092").split(",")


def green(value: Any) -> str:
    return f"\033[1;32m{value}\033[00m"
