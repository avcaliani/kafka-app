import json
from contextlib import contextmanager
from datetime import datetime

from kafka.producer.future import FutureRecordMetadata, RecordMetadata
from kafka_core.common import DATETIME_FORMAT, DEFAULT_SEVER, green

from kafka import KafkaProducer


def get_instance() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=[DEFAULT_SEVER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


@contextmanager
def new_producer():
    producer = get_instance()
    try:
        yield producer
    finally:
        producer.close()


def show_sent_message(
    response: FutureRecordMetadata, message: str = None, show_message: bool = False
) -> None:
    metadata: RecordMetadata = response.get()
    timestamp = datetime.utcfromtimestamp(metadata.timestamp / 1000)
    print(
        f"📦 "
        f"{green('T')}: {metadata.topic} | "
        f"{green('P')}: {metadata.partition} | "
        f"{green('O')}: {metadata.offset} | "
        f"{green('TS')}: {timestamp.strftime(DATETIME_FORMAT)}"
    )
    if show_message:
        print(f"{green('Message')}: {message}")
