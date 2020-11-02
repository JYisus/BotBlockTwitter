#!/usr/bin/python3

from twitter_bot import TwitterBot
from os import environ
import utils

API_KEY = utils.getenv('API_KEY','')
API_KEY_SECRET = utils.getenv('API_KEY_SECRET','')
ACCESS_TOKEN = utils.getenv('ACCESS_TOKEN','')
ACCESS_TOKEN_SECRET = utils.getenv('ACCESS_TOKEN_SECRET','')
STALKER_ACCOUNT = utils.getenv('STALKER_ACCOUNT','')
ACCOUNT = utils.getenv('ACCOUNT', '')

def check_credentials(credentials):
    not_empty_items = list( filter(lambda item: item != '', credentials))
    return len(not_empty_items) == len(credentials)

if __name__ == "__main__":
    credentials = {
        'api_key': API_KEY,
        'api_key_secret':API_KEY_SECRET,
        'access_token':ACCESS_TOKEN,
        'access_token_secret':ACCESS_TOKEN_SECRET
    }


    if check_credentials(credentials) & (STALKER_ACCOUNT != ''):
        bot = TwitterBot(credentials, ACCOUNT,STALKER_ACCOUNT)
        bot.block_followersOf_replying()
    else:
        print('Credenciales no validas')
