import json
from datetime import datetime
from uuid import uuid4

from kafka.producer.future import FutureRecordMetadata, RecordMetadata
from utils.color import green

from kafka import KafkaProducer

KAFKA_TOPIC = "ECOMMERCE_NEW_ORDER"
KAFKA_SERVERS = ["localhost:9092"]
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def showResponse(response: FutureRecordMetadata, message: str) -> None:
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


def run() -> None:
    print("🛒 New Order Service\nPress Ctrl+c to stop!")
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    try:
        msg = {
            "id": str(uuid4()),
            "items": [],
            "created_at": datetime.utcnow().strftime(DATETIME_FORMAT),
        }
        showResponse(producer.send(KAFKA_TOPIC, msg), msg)
    except (KeyboardInterrupt, SystemExit):
        producer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
