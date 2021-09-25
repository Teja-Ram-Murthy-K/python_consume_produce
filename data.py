from google_play_scraper import Sort, reviews_all
from faker import Faker
from pymongo import MongoClient
from json import loads
from kafka import KafkaConsumer
fake = Faker()

result = reviews_all(
    'com.havells.havellsone',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)

def get_registered_user():
        return {
            "name": fake.name(),
            "address": fake.address(),
            "created_at": fake.year()
        }

if __name__ == "__main__":
    print(result)
    # print(result())
    # print(result[1]['reviewId'])




