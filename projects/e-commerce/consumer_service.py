import json
from argparse import ArgumentParser, Namespace

from utils.display import show_received_message

from kafka import KafkaConsumer


def get_args():
    parser = ArgumentParser(description="Kafka Consumer")
    parser.add_argument("-n", "--name", dest="service_name", required=True)
    parser.add_argument("-g", "--group-id", dest="group_id", required=True)
    parser.add_argument(
        "-s", "--kafka-server", dest="kafka_server", default="localhost:9092"
    )
    parser.add_argument(
        "-t",
        "--topics",
        dest="topics",
        nargs="+",
        default=[],
        help="Topic for subscription.",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        dest="topic_pattern",
        help="Pattern to match available topics. You must provide either --topics or --pattern, but not both.",
    )
    return parser.parse_args()


def run(args: Namespace) -> None:
    print(f"\n{args.service_name.upper()}\nPress Ctrl+c to stop!")
    consumer = KafkaConsumer(
        bootstrap_servers=[args.kafka_server],
        group_id=args.group_id,
        value_deserializer=lambda msg: json.loads(msg.decode("utf-8")),
        enable_auto_commit=True,
        auto_offset_reset="earliest",
    )
    consumer.subscribe(topics=args.topics, pattern=args.topic_pattern)
    try:
        for msg in consumer:
            show_received_message(msg)
    except (KeyboardInterrupt, SystemExit):
        consumer.close()
        print("Bye bye!")


if __name__ == "__main__":
    run(get_args())
