# 📫 Kafka App

![License](https://img.shields.io/github/license/avcaliani/kafka-app?logo=apache&color=lightseagreen)

This is my Apache Kafka repository.  
Here you will find some stuff that I've done while I was learning about how to work with Apache Kafka.

## Repository Tags

- `v1.0` - Here you will find some PoCs that produce and consume data from Kafka developed in Spring Boot, PySpark and Python.
- `v2.0` - Here you will find the projects I've created while doing a Kafka course from Alura.

The `master` branch will have the most recent code that I've created, to check more details of a past development checkout the specific tag you want.

## Projects

- Project 01 - TBD

> ℹ️ To execute the projects you will need a Kafka instance running, to create your check the [next section](#quick-start).

### Quick Start

In this section we are going to up a local Kafka.

```bash
# Build & Up
docker-compose build && docker-compose up -d

# Logs
docker-compose logs kafka

# Shutting Down
docker-compose down
```

### Playground

Here are some terminal commands you can try to explore your own Kafka \o/

```bash
# Create your first topic \o/
docker-compose exec kafka kafka-topics.sh \
    --create \
    --bootstrap-server "localhost:9092" \
    --replication-factor "1" \
    --partitions "1" \
    --topic "MY_TOPIC"

# Check the available topics
docker-compose exec kafka kafka-topics.sh --list --bootstrap-server "localhost:9092"

# Producing messages ✉️
docker-compose exec kafka kafka-console-producer.sh \
    --broker-list "localhost:9092" \
    --topic "MY_TOPIC"

# Consuming messages 🔎
docker-compose exec kafka kafka-console-consumer.sh \
    --bootstrap-server "localhost:9092" \
    --topic "MY_TOPIC" --from-beginning

# Cheking our topics
docker-compose exec kafka kafka-consumer-groups.sh \
    --all-groups \
    --describe \
    --bootstrap-server "localhost:9092"
```

## Useful Links

- [Apache Kafka](https://kafka.apache.org/downloads)
- [Kafka Tool - UI Tool 4 Kafka](https://www.kafkatool.com/download.html)
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)

<br/>

🧙‍♂️ _"If in doubt Meriadoc, always follow your nose." - Gandalf_
