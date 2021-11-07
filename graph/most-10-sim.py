from gensim.models import doc2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import logging
import json
#from collections import defaultdict
import operator


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model1 = Doc2Vec.load(r'G:\twitter\Twitter\golduser.model')

f = open(r'G:\twitter\Twitter\uusers.json')
df = json.loads(f.read())
users = df['users']

d = dict()

for u in users:
    try:
        d[u]=(map(lambda x:x[0],model1.docvecs.most_similar(str(u).lstrip())))
    except:
        continue

with open('links.json','w')as jj:
    json.dump(d,jj)

