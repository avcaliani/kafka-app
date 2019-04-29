# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
from kafka import KafkaProducer # pip install kafka-python
import json
import random
from time import sleep
from datetime import datetime

# Create an instance of the Kafka producer
producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = lambda v: str(v).encode('utf-8')
)

# Call the producer.send method with a producer-record
print("KAFKA PRODUCER - Press Ctrl+c to stop")

for i in range(1000):
    value = { 'number': i }
    producer.send('python-topic', value)
    print(f'Message {i + 1} sent!')
    sleep(5)
    