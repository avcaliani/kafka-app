# 💬 Apache Kafka
By Anthony Vilarim Caliani

![#](https://img.shields.io/badge/license-MIT-blue.svg)

This is my Apache Kafka repository. Here you will find some stuff that I've done while I was learning about how to work with Apache Kafka.

## Quick Start
```bash
# Create Kafka and Zookeper containers
docker-compose up -d

# Checking if everything is okay
docker-compose ps

# Checking Zookeper
docker-compose logs zookeeper | grep -i binding

# Checking Kafka (It may take a few seconds to start)
docker-compose logs kafka | grep -i started
```

### Optional Steps
```bash
./kafka.sh --create "my-topic"
./kafka.sh --describe "my-topic"
./kafka.sh --test-pub "my-topic"
./kafka.sh --test-sub "my-topic"
```

## Kafka Tool

![#](.docs/kafkatool-props-1.png)

![#](.docs/kafkatool-props-2.png)

![#](.docs/kafkatool-messages.png)


### Related Links
- [Kafka Tool - UI Tool 4 Kafka](https://www.kafkatool.com/download.html)
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)

---

🧙‍♂️ _"If in doubt Meriadoc, always follow your nose." - Gandalf_
