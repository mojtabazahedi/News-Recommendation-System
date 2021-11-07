__author__ = 'mojtaba'
import tweepy
import sqlite3
import  time
########################################################
db = sqlite3.connect('NewsData.db')
dbcursor = db.cursor()
############################################################
#id_data = []
#textfile = open('usertest', "r")
#id_data = textfile.read().split(',')


auth = tweepy.OAuthHandler('##','##')
auth.set_access_token('##-##','##')

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline,id='washingtonpost' ,include_rts = 'true',include_entities='true').items(100000):

            dbcursor.execute('''INSERT INTO news ( tweetid,geo, date, text, retweet, 'language',channelname) VALUES(?,?,?,?,?,?,?)''', (tweet.id ,str(tweet.geo), tweet.created_at, tweet.text, tweet.retweeted, str(tweet.lang),'washingtonpost'))
            db.commit()

db.close()
