import tweepy
from tweepy.auth import OAuthHandler

consumer_key = "wZ2q7JPDcfg3BfoAPFAMDJrPE"
consumer_secret = "ZJfZRLp5PZOVQlKFJTEwzPRXjYZcA1weHoFOlHDQydEhDmLbx1"
access_token = "608653541-LgMjkTeZM0hbmjkoWq9uHG73ERWsyIlNNwjDtywz"
access_token_secret = "Mx32YYgZEKug6zdA0Uo0IVmn41CRTLPG43mAcigENjY6B"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text