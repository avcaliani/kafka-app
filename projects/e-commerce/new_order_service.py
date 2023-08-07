import json
from datetime import datetime
from random import randint
from typing import Tuple
from uuid import uuid4
from time import sleep

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
    n_messages = randint(10, 1000) 
    print(f"Messages to be sent 👉 {n_messages}")
    try:
        for _ in range(0, n_messages):
            email_msg, order_msg = new_order()
            customer_id = bytes(order_msg["customer_id"], "utf-8")
            show_sent_message(
                producer.send(topic="ECOMMERCE_NEW_ORDER", key=customer_id, value=order_msg), 
                order_msg
            )
            show_sent_message(
                producer.send(topic="ECOMMERCE_NEW_EMAIL", key=customer_id, value=email_msg), 
                email_msg
            )
            sleep(randint(0, 10) / 10)
        print(f"\n{n_messages} messages sent ✅")
    except (KeyboardInterrupt, SystemExit):
        print("Bye bye!")
    finally:
        producer.close()


if __name__ == "__main__":
    run()
