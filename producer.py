from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x, default=vars).encode('UTF-8')
)


class MyData:
    def __init__(self, j: int):
        self.iteration = j
        self.date = datetime.now().date().__str__()
        self.time = datetime.now().time().__str__()
    iteration: 0
    date: "_"
    time: "_"


for j in range(1000):
    data = MyData(j+1)
    producer.send('topic', value=data)
    sleep(0.01)

print("Send "+(j+1).__str__()+" messages")
