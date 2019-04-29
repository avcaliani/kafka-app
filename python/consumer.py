# @author     Anthony Vilarim Caliani
# @github     github.com/avcaliani
from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    'python-topic',
    bootstrap_servers=['localhost:9092']
)

for msg in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    decoded = None
    try:
        decoded = msg.value.decode('utf-8')
    except expression as identifier:
        decoded = 'Unable to parse'
    print (
        "%s:%d:%d: key=%s value=%s" % (
            msg.topic, msg.partition, msg.offset, msg.key, decoded
        )
    )