import tweepy
from textblob import TextBlob
import json
from pathlib import Path
from pprint import pprint

home = str(Path.home())
with open('%s/.twitter/twitter_sentiment1111.json' % home) as f:
    tw_config = json.load(f)


consumer_key = tw_config['consumer_key']
consumer_secret = tw_config['consumer_secret']
access_token = tw_config['access_token']
access_token_secret = tw_config['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
# pprint(consumer_secret)



