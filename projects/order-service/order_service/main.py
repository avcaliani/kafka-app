from datetime import datetime
from random import randint, random
from time import sleep
from typing import Tuple
from uuid import uuid4

import names
from kafka_core.common import DATETIME_FORMAT
from kafka_core.producer import new_producer, show_sent_message


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
        "total": round(random() * randint(100, 10000), 2),
        "created_at": datetime.utcnow().strftime(DATETIME_FORMAT),
    }
    return email_msg, order_msg


def run() -> None:
    n_messages = randint(5, 10)
    print(f"Messages to be sent 👉 {n_messages}")
    with new_producer() as producer:
        for _ in range(0, n_messages):
            email_msg, order_msg = new_order()
            message_key = bytes(order_msg["customer_id"], "utf-8")
            show_sent_message(
                producer.send(
                    topic="ECOMMERCE_NEW_ORDER", key=message_key, value=order_msg
                )
            )
            show_sent_message(
                producer.send(
                    topic="ECOMMERCE_NEW_EMAIL", key=message_key, value=email_msg
                )
            )
            sleep(randint(0, 10) / 10)
        print(f"\n{n_messages} messages sent ✅")


if __name__ == "__main__":
    print("📦 NEW ORDER SERVICE\nPress Ctrl+c to stop!")
    try:
        run()
    except (KeyboardInterrupt, SystemExit):
        print("Bye bye!")
