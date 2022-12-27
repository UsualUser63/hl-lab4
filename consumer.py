from kafka import KafkaConsumer
from json import loads

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
