import json

from utils.display import show_received_message

from kafka import KafkaConsumer

KAFKA_TOPIC = "ECOMMERCE_NEW_EMAIL"


def run() -> None:
    print(f"📧 E-MAIL SERVICE\nPress Ctrl+c to stop!")
    consumer = KafkaConsumer(
        bootstrap_servers=["localhost:9092"],
        group_id="email-service",
        value_deserializer=lambda msg: json.loads(msg.decode("utf-8")),
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )
    consumer.subscribe([KAFKA_TOPIC])
    try:
        for msg in consumer:
            show_received_message(msg)
    except (KeyboardInterrupt, SystemExit):
        consumer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
