from kafka_core.consumer import new_consumer, show_received_message
from kafka_core.producer import new_producer, show_sent_message


def is_fraud(message: dict) -> bool:
    order_total = message.get("total")
    return not order_total or order_total > 5000


def run() -> None:
    with new_consumer(
        group_id="fraud-service", topics=["ECOMMERCE_NEW_ORDER"]
    ) as consumer:
        with new_producer() as producer:
            for msg in consumer:
                show_received_message(msg)
                order = msg.value
                
                topic_name = "ECOMMERCE_ORDER_ACCEPTED"
                if is_fraud(order):
                    topic_name = "ECOMMERCE_ORDER_REJECTED"
                    print("🚩 Fraud Detected\n")
                    
                show_sent_message(
                    producer.send(
                        topic=topic_name, 
                        key=bytes(order.get("customer_email"), "utf-8"), 
                        value=order
                    )
                )


if __name__ == "__main__":
    print("🕵️‍♂️ FRAUD SERVICE\nPress Ctrl+c to stop!")
    try:
        run()
    except (KeyboardInterrupt, SystemExit):
        print("Bye bye!")
