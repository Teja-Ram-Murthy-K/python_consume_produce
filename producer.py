from kafka import KafkaProducer
from bson import json_util
import json
from data import  result
import time

def json_serializer(data):
    return json.dumps(data, default=json_util.default).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=json_serializer)
if __name__ == "__main__":
        for i in range(len(result)):
            registered_user = result[i]
            print(registered_user)
            producer.send("test", registered_user)
            time.sleep(4)