# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
from json import loads


# Import sys module
import sys

# Import json module to serialize data
import json

# Initialize consumer variable and set property for JSON decode
consumer = KafkaConsumer ('test',bootstrap_servers = ['localhost:29092'],
value_deserializer=lambda m: m)
# value_deserializer=lambda x: loads(x.decode('utf-8')))
# Read data from kafka
for message in consumer:
    print("Consumer records:\n")
    print(message)
# Terminate the script
sys.exit()