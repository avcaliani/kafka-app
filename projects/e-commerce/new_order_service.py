import json
from datetime import datetime
from typing import Tuple
from uuid import uuid4

import names
from utils.display import DATETIME_FORMAT, show_sent_message

from kafka import KafkaProducer


def new_order() -> Tuple[dict, dict]:
    customer_id = str(uuid4())
    customer_name = names.get_full_name()
    email_msg = {
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_email": f"{customer_name.replace(' ', '.').lower()}@github.com",
        "email_template": "template__new_order",
    }
    order_msg = {
        "id": str(uuid4()),
        "customer_id": customer_id,
        "items": [],
        "created_at": datetime.utcnow().strftime(DATETIME_FORMAT),
    }
    return email_msg, order_msg


def run() -> None:
    print("🛒 NEW ORDER SERVICE\nPress Ctrl+c to stop!")
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    try:
        email_msg, order_msg = new_order()
        show_sent_message(
            producer.send(topic="ECOMMERCE_NEW_ORDER", value=order_msg), order_msg
        )
        show_sent_message(
            producer.send(topic="ECOMMERCE_NEW_EMAIL", value=email_msg), email_msg
        )
    except (KeyboardInterrupt, SystemExit):
        producer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
