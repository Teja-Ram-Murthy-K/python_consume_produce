# from google_play_scraper import Sort, reviews

# result, continuation_token = reviews(
#     'com.havells.havellsone',
#     lang='en', # defaults to 'en'
#     country='us', # defaults to 'us'
#     sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
#     # count=10, # defaults to 100
#     filter_score_with=5 # defaults to None(means all score)
# )

# # If you pass `continuation_token` as an argument to the reviews function at this point,
# # it will crawl the items after 3 review items.

# result, _ = reviews(
#     'com.havells.havellsone',
#     continuation_token=continuation_token # defaults to None(load from the beginning)
# )

from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.havells.havellsone',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)
print(result)
print(result[1]['reviewId'])
