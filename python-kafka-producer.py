from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
csvFilePath = 'python/mstatistics.csv'

data = []
with open(csvFilePath, "rb") as csvfile:
    data = csvfile.readlines()
    for rec in data:
        print("sending record",rec)
        producer.send('csvdata', rec) #bytes sent
        print("sent record")