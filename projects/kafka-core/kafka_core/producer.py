import json
from contextlib import contextmanager
from datetime import datetime

from kafka.producer.future import FutureRecordMetadata, RecordMetadata
from kafka_core.common import DATETIME_FORMAT, DEFAULT_SEVER, green

from kafka import KafkaProducer


@contextmanager
def new_producer() -> KafkaProducer:
    producer = KafkaProducer(
        bootstrap_servers=[DEFAULT_SEVER],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    try:
        yield producer
    finally:
        producer.close()


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
