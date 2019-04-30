# Spring Kafka
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/license-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/java-1.8-red.svg)](#) [![#](https://img.shields.io/badge/spring--boot-2.1.4.RELEASE-green.svg)](#)

## Running
Run `mvn clean install` and then `java -jar target/spring-kafka-19.04.01.jar`. 

Now you can send a `POST` Request to `http://localhost:8080/message` passing your message in request body.

**ATTENTION**: Keep your eyes on application console, because everything will be logged 😉

---

## Project Map
```
.
├── mvnw
├── mvnw.cmd
├── pom.xml
├── README.md
└── src
    └── main
        ├── java
        │   └── br
        │       └── avcaliani
        │           └── springkafka
        │               ├── controller
        │               │   └── MessageController.java
        │               ├── kafka
        │               │   ├── Consumer.java
        │               │   └── Producer.java
        │               └── SpringKafkaApplication.java
        └── resources
            └── application.properties
```

---

## Related Links
- [Spring Docs: Kafka Client Compatibility](https://spring.io/projects/spring-kafka)
- [Spring Docs: Apache Kafka](https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-messaging.html#boot-features-kafka)

---

_You can find [@avcaliani](#) at [GitHub](https://github.com/avcaliani) or [GitLab](https://gitlab.com/avcaliani)._
