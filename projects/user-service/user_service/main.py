from kafka_core.consumer import new_consumer, show_received_message


def run() -> None:
    with new_consumer(group_id="user-service", topics=["ECOMMERCE_NEW_ORDER"]) as consumer:
        for msg in consumer:
            show_received_message(msg)


if __name__ == "__main__":
    print("☃️ USER SERVICE\nPress Ctrl+c to stop!")
    try:
        run()
    except (KeyboardInterrupt, SystemExit):
        print("Bye bye!")
