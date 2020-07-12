# simple-python-kafka
- simple python kafka app with setup mentioned below .
- producer produces contents of csv to a topic
- consumer consumes contents and pushes to a mongoDb through pyMongo client

# download link
 - https://kafka.apache.org/downloads

# Paste the contents in your 
 - C:\<kafka_2.13-2.5.0>

# cmd
 - cd C:\kafka_2.13-2.5.0
 - bin\windows\zookeeper-server-start.bat config\zookeeper.properties
 - bin\windows\kafka-server-start.bat config\server.properties

# few info
 - Topic - > (communication channel) -> use of partitions allowed
 - Producer - > push data - > Consumer registered picks it.
 
# create topic
 - bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --partitions 1 --replication-factor 1 --topic csvdata
# list topic
 - bin\windows\kafka-topics.bat --list --zookeeper localhost:2181
# producer
 - bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic csvdata
# consumer
 - bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic csvdata
# pushing files
 - bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic csvdata < mstatistics.csv
