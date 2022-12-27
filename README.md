# hl-lab4
Лабораторная №4

Автор: Катюшкина Алина (МО-191)

Сначала создаем контейнеры для kafka : 

docker-compose up -d 

Потом создаем топик с помощью команды :

docker exec broker kafka-topics --bootstrap-server broker:9092 --create --topic topic

А также устанваливаем kafka для питона :

pip install kafka-python

Теперь можно запустить producer.py :

python producer.py

consumer.py запуcкается аналогично
