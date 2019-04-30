package br.avcaliani.springkafka.controller;

import br.avcaliani.springkafka.kafka.Consumer;
import br.avcaliani.springkafka.kafka.Producer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/message")
public class MessageController {

    @Autowired
    private Producer producer;

    @PostMapping
    public boolean publish(@RequestBody String message) {
        producer.send(message);
        return true;
    }
}