from datetime import datetime

from kafka.consumer.fetcher import ConsumerRecord
from kafka.producer.future import FutureRecordMetadata, RecordMetadata

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

from typing import Any


def green(value: Any) -> str:
    return f"\033[1;32m{value}\033[00m"


def show_sent_message(response: FutureRecordMetadata, message: str) -> None:
    metadata: RecordMetadata = response.get()
    timestamp = datetime.utcfromtimestamp(metadata.timestamp / 1000)
    print(
        f"📦 "
        f"{green('Topic')}: {metadata.topic} | "
        f"{green('Partition')}: {metadata.partition} | "
        f"{green('Offset')}: {metadata.offset} | "
        f"{green('Timestamp')}: {timestamp.strftime(DATETIME_FORMAT)} | "
        f"{green('Message')}: {message}"
    )


def show_received_message(message: ConsumerRecord) -> None:
    timestamp = datetime.utcfromtimestamp(message.timestamp / 1000)
    print(
        f"✉️ "
        f"{green('Topic')}: {message.topic} | "
        f"{green('Partition')}: {message.partition} | "
        f"{green('Offset')}: {message.offset} | "
        f"{green('Key')}: {message.key} | "
        f"{green('Timestamp')}: {timestamp.strftime(DATETIME_FORMAT)} | "
        f"{green('Message')}: {message.value}"
    )
