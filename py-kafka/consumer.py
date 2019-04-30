import json
from kafka import KafkaConsumer
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

KAFKA CONSUMER 👀
Press Ctrl+c to stop
""")

consumer = KafkaConsumer(
  bootstrap_servers=['localhost:9092'],
  group_id='group-python',
  value_deserializer=lambda msg: json.loads(msg.decode('utf-8')),
  enable_auto_commit=False,
  auto_offset_reset='earliest'
)
consumer.subscribe([ TOPIC ])

try:
  for msg in consumer:
    err = msg.value['number'] % 3 == 0 # Fake Error
    if err:
      print(f'ERROR! Rejected message -> { msg.value }')
    else:
      print ('%s:%d:%d: key=%s value=%s' % (
        msg.topic, msg.partition, msg.offset, msg.key, msg.value
      ))
      consumer.commit()

except (KeyboardInterrupt, SystemExit):
  consumer.close()
  print('Bye bye!')
