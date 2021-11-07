import time
import tweepy

auth = tweepy.OAuthHandler('lYbgMGCMDDBwoLwWVTqtWf13S', 'lm1TTF4dcDcAywcMlfTx5bwEr0XmyCCkH2SWnnVgOzOvyaqCnH')
auth.set_access_token('281509185-FskWAabWsm3ellGqDUYgjgaXv5zXw4HkV43uX3wU', '4JplyZRuSdni2b1FDdaIKeptOpCit45jYzxvlVwKJvYPV')

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="Bloomingdales").pages():
        ids.extend(page)
        # time.sleep(60)

        if len(page) == 5000: time.sleep(60)
        # txt = open("thefile.txt", 'w')
        for x in ids:
            str1 = str(x)
            print (str1 + ",")
        ids = []