import tweepy
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
tweet = "Phew, not sure what happened there, bring on hump day!"
try:
    client.create_tweet(text=tweet)
    print("Posted tweet!")
except tweepy.errors as e:
    print(f"Error: {str(e)}")
