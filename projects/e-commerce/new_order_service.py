import json
from datetime import datetime
from typing import Tuple
from uuid import uuid4

import names
from kafka.producer.future import FutureRecordMetadata, RecordMetadata
from utils.color import green

from kafka import KafkaProducer

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


def new_order() -> Tuple[dict, dict]:
    customer_id = str(uuid4())
    customer_name = names.get_full_name()
    email_msg = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_email": f"{customer_name.replace(' ', '.').lower()}@github.com",
        "email_template": "template__new_order"
    }
    order_msg = {
        "id": str(uuid4()),
        "customer_id": customer_id,
        "items": [],
        "created_at": datetime.utcnow().strftime(DATETIME_FORMAT),
    }
    return email_msg, order_msg


def run() -> None:
    print("🛒 New Order Service\nPress Ctrl+c to stop!")
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    try:
        email_msg, order_msg = new_order()
        showResponse(producer.send(topic="ECOMMERCE_NEW_ORDER", value=order_msg), order_msg)
        showResponse(producer.send(topic="ECOMMERCE_NEW_EMAIL", value=email_msg), email_msg)
    except (KeyboardInterrupt, SystemExit):
        producer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
