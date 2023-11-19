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


def show_sent_message(response: FutureRecordMetadata, message: str = None) -> None:
    metadata: RecordMetadata = response.get()
    timestamp = datetime.utcfromtimestamp(metadata.timestamp / 1000)
    log_msg = (
        f"📦 New Message Sent\n"
        f"├─ {green('Topic')}: {metadata.topic}\n"
        f"├─ {green('Partition')}: {metadata.partition} / {green('Offset')}: {metadata.offset}\n"
    )
    time_log = f"{green('Timestamp')}: {timestamp.strftime(DATETIME_FORMAT)}"
    if message:
        log_msg += f"├─ {time_log}\n└─ {green('Message')}: {message}\n"
    else:
        log_msg += f"└─ {time_log}\n"
    print(log_msg)
