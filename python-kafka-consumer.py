from datetime import datetime
from kafka import KafkaConsumer
from pymongo import MongoClient

consumer = KafkaConsumer('csvdata',bootstrap_servers=['localhost:9092'],api_version=(0, 10))
client = MongoClient(port=27017)
db = client.mitdb
print(db.list_collection_names())
collection = db.list_collection_names()[0]

timestamp = datetime.now()
result = {}
csv_data = []
header_arr = ['id','timestamp','pkt_in_bytes','pkt_out_bytes']

for message in consumer:
    print(message)
    csv_data = str(message.value).split(',')
    data = {header_arr[i] : str(csv_data[i]) for i in range(len(header_arr))}
    result = db.csvstats.insert_one(data)
    current_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    print("current_time {}: inserted into collection {} , id {}".format(current_time,collection, result.inserted_id))





