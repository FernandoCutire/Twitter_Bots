# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

#Add your credentials here
twitter_keys = {
        'consumer_key':        'uw9LFBUG68eTQ9WbOxDqIceNr',
        'consumer_secret':     'XZbN2YE6teESsBjRNY2AG9JYhbvPqmvv798rIejM4Lg9xdWmhd',
        'access_token_key':    '4492109894-vMXUD1of3x3CacjPVn4sikXEnGuNDwuwjZjVn2d',
        'access_token_secret': 'xDm3uliQkViSfKn4XgFcmXjkzhwL6w5pmcXUEhoN7C2uu'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

def create_api():
    # Add your credentials here
    twitter_keys = {
        'consumer_key': 'uw9LFBUG68eTQ9WbOxDqIceNr',
        'consumer_secret': 'XZbN2YE6teESsBjRNY2AG9JYhbvPqmvv798rIejM4Lg9xdWmhd',
        'access_token_key': '4492109894-vMXUD1of3x3CacjPVn4sikXEnGuNDwuwjZjVn2d',
        'access_token_secret': 'xDm3uliQkViSfKn4XgFcmXjkzhwL6w5pmcXUEhoN7C2uu'
    }

    # Setup access to API
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api





