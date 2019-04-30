import json
from kafka import KafkaProducer
from time import sleep
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


TOPIC = 'python-topic'

print("""
 ____           _  __         __  _           
|  _ \  _   _  | |/ /  __ _  / _|| | __  __ _ 
| |_) || | | | | ' /  / _` || |_ | |/ / / _` |
|  __/ | |_| | | . \ | (_| ||  _||   < | (_| |
|_|     \__, | |_|\_\ \__,_||_|  |_|\_\ \__,_|
        |___/                    by @avcaliani

KAFKA PRODUCER 😴
Press Ctrl+c to stop
""")

producer = KafkaProducer(
  bootstrap_servers = ['localhost:9092'],
  value_serializer = lambda v: json.dumps(v).encode('utf-8')
)

try:
  for i in range(1000):
    producer.send(TOPIC, { 'number': i })
    print(f'Message {i + 1} sent!')
    sleep(5)
except (KeyboardInterrupt, SystemExit):
  producer.close()
  print('Bye bye!')
    
