from gensim.models import doc2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import logging
import json
#from collections import defaultdict
import operator


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model1 = Doc2Vec.load(r'G:\twitter\Twitter\tweetsdoc.model')

f = open(r'G:\twitter\Twitter\alltweet.json')
df = json.loads(f.read())
tweet = df['tweet']

d = dict()

for t in tweet:

        d[t]=(map(lambda x:x[0],model1.docvecs.most_similar(str(t).lstrip())))


with open('tweetlink.json','w')as jj:
    json.dump(d,jj)

