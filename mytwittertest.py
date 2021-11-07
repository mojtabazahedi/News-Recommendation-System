__author__ = 'Reza'
import tweepy

auth = tweepy.OAuthHandler('lYbgMGCMDDBwoLwWVTqtWf13S', 'lm1TTF4dcDcAywcMlfTx5bwEr0XmyCCkH2SWnnVgOzOvyaqCnH')
auth.set_access_token('281509185-FskWAabWsm3ellGqDUYgjgaXv5zXw4HkV43uX3wU', '4JplyZRuSdni2b1FDdaIKeptOpCit45jYzxvlVwKJvYPV')

api = tweepy.API(auth)
print api.rate_limit_status()