import os

import tweepy
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.



consumer_key=os.getenv("API_KEY")
consumer_secret=os.getenv("API_SECRET_KEY")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
