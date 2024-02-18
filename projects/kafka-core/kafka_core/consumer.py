import json
from contextlib import contextmanager
from datetime import datetime

from kafka.consumer.fetcher import ConsumerRecord
from kafka_core.common import DATETIME_FORMAT, DEFAULT_SEVER, green

from kafka import KafkaConsumer


@contextmanager
def new_consumer(
    group_id: str, topics: list = None, topic_pattern: str = None
) -> KafkaConsumer:
    consumer = KafkaConsumer(
        bootstrap_servers=[DEFAULT_SEVER],
        group_id=group_id,
        value_deserializer=lambda msg: json.loads(msg.decode("utf-8")),
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )

    if (topics and topic_pattern) or (not topics and not topic_pattern):
        raise RuntimeError(
            "You must provide either 'topics' or 'topic_pattern', but not both."
        )

    consumer.subscribe(topics=topics, pattern=topic_pattern)
    try:
        yield consumer
    finally:
        consumer.close()


def show_received_message(message: ConsumerRecord, show_message: bool = False) -> None:
    timestamp = datetime.utcfromtimestamp(message.timestamp / 1000)
    print(
        f"✉️ "
        f"{green('T')}: {message.topic} | "
        f"{green('P')}: {message.partition} | "
        f"{green('O')}: {message.offset} | "
        f"{green('K')}: {message.key.decode('utf-8')} | "
        f"{green('TS')}: {timestamp.strftime(DATETIME_FORMAT)}"
    )
    if show_message:
        print(f"{green('Message')}: {message.value}")
