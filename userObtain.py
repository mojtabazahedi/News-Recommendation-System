__author__ = 'Reza'
import tweepy
import sqlite3
import  time
########################################################
db = sqlite3.connect('NewsData.db')
dbcursor = db.cursor()
############################################################
id_data = []
textfile = open('usertest', "r")
id_data = textfile.read().split(',')


auth = tweepy.OAuthHandler('6FRXSvQkWQk1P99u1pDERiIix','MYRbkkYYJ9F6Oc6TRPBWDrPH3xwmDAVBviKoXB31kcnzc3QNPl')
auth.set_access_token('252507171-VQB2mJ48DiVHNFPZG4JW8wWz9GizvTQbYgn5R8dT','aEjrrpC5ZjBy8Zxyui5ly76G5YzqjNRBxSIDuDQphQGDQ')

api = tweepy.API(auth)
for uid in id_data :
   c = tweepy.Cursor(api.user_timeline, id=uid , include_rts = 'true',include_entities='true').items(10000)
   while True:
    try:
        tweet = c.next()
        dbcursor.execute('''INSERT INTO news ( tweetid,geo, date, text, retweet, 'language',channelname) VALUES(?,?,?,?,?,?,?)''', (tweet.id ,str(tweet.geo), tweet.created_at, tweet.text, tweet.retweeted, str(tweet.lang),'espn'))
        db.commit()
    except tweepy.RateLimitError:
        time.sleep(60 * 15)
        continue
    except tweepy.TweepError:
        break
    except StopIteration:
        break


db.close()