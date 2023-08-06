import json
from datetime import datetime

from kafka.consumer.fetcher import ConsumerRecord
from utils.color import green

from kafka import KafkaConsumer

KAFKA_TOPIC = "ECOMMERCE_NEW_ORDER"
KAFKA_SERVERS = ["localhost:9092"]
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def showMessage(message: ConsumerRecord) -> None:
    timestamp = datetime.utcfromtimestamp(message.timestamp / 1000)
    print(
        f"✉️ "
        f"{green('Topic')}: {message.topic} | "
        f"{green('Partition')}: {message.partition} | "
        f"{green('Offset')}: {message.offset} | "
        f"{green('Timestamp')}: {timestamp.strftime(DATETIME_FORMAT)} | "
        f"{green('Message')}: {message.value}"
    )


def run() -> None:
    print("🕵️ Fraud Detector Service\nPress Ctrl+c to stop!")
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVERS,
        group_id="fraud-detector-service",
        value_deserializer=lambda msg: json.loads(msg.decode("utf-8")),
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )
    consumer.subscribe([KAFKA_TOPIC])
    try:
        for msg in consumer:
            showMessage(msg)
    except (KeyboardInterrupt, SystemExit):
        consumer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
