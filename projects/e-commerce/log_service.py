import json

from utils.display import show_received_message

from kafka import KafkaConsumer

KAFKA_TOPIC = "ECOMMERCE*"


def run() -> None:
    print("📄 LOG SERVICE\nPress Ctrl+c to stop!")
    consumer = KafkaConsumer(
        bootstrap_servers=["localhost:9092"],
        group_id="log-service",
        value_deserializer=lambda msg: json.loads(msg.decode("utf-8")),
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )
    consumer.subscribe(pattern=KAFKA_TOPIC)
    try:
        for msg in consumer:
            show_received_message(msg)
    except (KeyboardInterrupt, SystemExit):
        consumer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run()
