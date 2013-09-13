import tweepy
import json
import jsonpickle
from pprint import pprint
import os

 
# Consumer keys and access tokens, used for OAuth
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

ct = 0
tweets = []
for tweet in tweepy.Cursor(api.search, q="#tcdisrupt", count=100, include_entities=True, lang="en").items():
	print ct
	tweets.append(tweet)
	if ct > 100:
		break
	ct += 1

# Sample method, used to update a status
# data = api.search("#regurgitate")

pickled = jsonpickle.encode(tweets)
with open("raw-tweets.json", "w") as jsonfile:
	jsonfile.write(json.dumps(json.loads(pickled), indent=4, sort_keys=True))