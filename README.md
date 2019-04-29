# Apache Kafka
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/docker-18.09.2-dodgerblue.svg)](#) [![#](https://img.shields.io/badge/docker--compose-1.23.2-royalblue.svg)](#) [![#](https://img.shields.io/badge/apache--kafka-latest-lightgray.svg)](#) [![#](https://img.shields.io/badge/zookeper-latest-darkolivegreen.svg)](#)

## Repository Description
This is my Apache Kafka repository. Here you will find some stuff that I've done while I was learning about how to work with Apache Kafka.

## Running
```sh
# Create Kafka and Zookeper containers
cd docker && docker-compose up -d

# Checking if everything is okay
docker-compose ps

# Checking Zookeper
docker-compose logs zookeeper | grep -i binding

# Checking Kafka (It may take a few seconds to start)
docker-compose logs kafka | grep -i started

#
# OPTIONAL STEPS
#
# Topic Name: my-topic
# Zookeper Port and Kafka Port are defined on 'docker/docker-compose.yml'

# Creating a topic in Kafka
docker-compose exec kafka \
    kafka-topics --create \
    --topic my-topic \
    --partitions 1 \
    --replication-factor 1 \
    --if-not-exists \
    --zookeeper localhost:32181

# Checking if our topic was created
docker-compose exec kafka  \
  kafka-topics --describe \
  --topic my-topic \
  --zookeeper localhost:32181

# Producing messages
docker-compose exec kafka  \
  bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list localhost:29092 --topic my-topic && echo 'Produced 100 messages.'"

# Consuming messages
docker-compose exec kafka  \
  kafka-console-consumer \
  --bootstrap-server localhost:29092 \
  --topic my-topic \
  --from-beginning \
  --max-messages 100

# THE END
```

## Repository Projects
- **X**: Soon...

## Projects Map

### X
```
X/
└── ???
```

---

## External Links
- [Medium: Aprendendo na prática](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
- [Github: Confluent Inc. (Apache Kafka®)](https://github.com/confluentinc/cp-docker-images)

---

_You can find [@avcaliani](#) at [GitHub](https://github.com/avcaliani) or [GitLab](https://gitlab.com/avcaliani)._
