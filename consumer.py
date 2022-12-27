# Прежде чем запускать код создаем топик с помощью команды :
# docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic topic
# А также устанваливаем kafka для питона :
# pip install kafka-python
from kafka import KafkaConsumer
from json import loads
from time import sleep
consumer = KafkaConsumer(
    'topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=5000
)

sum = 0

for event in consumer:
    event_data = event.value
    sum += 1
    print(event_data)

print("Количество сообщений: "+sum.__str__())
