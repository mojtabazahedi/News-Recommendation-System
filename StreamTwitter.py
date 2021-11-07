__author__ = 'Reza'
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
auth = tweepy.OAuthHandler('lYbgMGCMDDBwoLwWVTqtWf13S', 'lm1TTF4dcDcAywcMlfTx5bwEr0XmyCCkH2SWnnVgOzOvyaqCnH')
auth.set_access_token('281509185-FskWAabWsm3ellGqDUYgjgaXv5zXw4HkV43uX3wU', '4JplyZRuSdni2b1FDdaIKeptOpCit45jYzxvlVwKJvYPV')
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    stream = Stream(auth, l)
    stream.filter(track=['iphone 6', 'sony xperia z5', 'htc one m9'])