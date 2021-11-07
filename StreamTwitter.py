
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
auth = tweepy.OAuthHandler('##', '##')
auth.set_access_token('##', '##')
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
