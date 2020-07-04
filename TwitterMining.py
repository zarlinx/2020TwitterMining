import json
import tweepy
from tweepy import OAuthHandler

def process_or_store(tweet):
    print(json.dumps(tweet))


consumer_key = '9GRtT2W5K2ia7ha1iXhxb4Jly'
consumer_secret = 'lGhBgDgcEzhe54DS43Q0Si3HYJJgjIKR89DKavNa7fZHyqMqMv'
access_token = '1083100857686740992-vFAJ7Bcbi4BSowBIqYR7HxyuYY8Cui'
access_secret = 'qVrABTam1S4z9EiF2P0cIk7WXBSTu1QWkKb0lVN35rfrC'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)