package br.avcaliani.springkafka.kafka;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class Consumer {

    private static final Logger L = LoggerFactory.getLogger(Consumer.class);

    @KafkaListener(topics = "${app.kafka.topic}")
    public void receive(ConsumerRecord<?, ?> consumerRecord) {
        L.info("received data='{}'", consumerRecord.toString());
    }
}
