#import modules
import configparser
import os
import tweepy
import pandas as pd
from tqdm import tqdm

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#aunthenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#Get twitter account
all_congress_accounts = pd.read_csv('data/cong_accounts.csv')
all_congress_accounts.head()

#Get n recent tweets from user
def get_n_tweets(user,n):
    tweets = []
    columns = ['User', 'Content', 'Date', 'Favs', 'RTs']

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=user).items(n):
        tweets.append([tweet.user.screen_name,
                       tweet.text,
                       tweet.created_at,
                       tweet.favorite_count,
                       tweet.retweet_count])
        tempdf = pd.DataFrame(tweets, columns=columns)
        return tempdf

all_congress_tweets = pd.DataFrame()
no_accts = []
for cong in tqdm(all_congress_accounts.Acct):
    try:
        temp_tweets = get_n_tweets(cong,2)
        all_congress_tweets = pd.concat([all_congress_tweets, temp_tweets])
        print('Gathering data')
    except:
        no_accts.append(cong)
        print(f'{cong} account is not active or does not have tweets')


all_congress_tweets.to_csv('data/all_cong_tweets.csv', encoding='utf-8', index=False)
all_congress_tweets.head(10)
            
