__author__ = 'mojtaba'
import gensim
from gensim.models import doc2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import logging
import sqlite3
import json
#######################
#db = sqlite3.connect('TwitterData1')
#c = db.cursor()
f = open(r'G:\twitter\Twitter\user-tweet.json')
df = json.loads(f.read())
g= open(r'G:\twitter\Twitter\uusers.json')
dg = json.loads(g.read())
users = dg['users']

#########
d = dict()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model1 = Doc2Vec.load('u-t.model')
##############################################
#u = '346916581'
for u in users:
    new_doc_vec = model1.docvecs.most_similar(str(u).lstrip(),topn=600)
    flist = filter(lambda  a :a[0] not in df[u] and  a[0] not in users,new_doc_vec)
    d[str(u).lstrip()]=(((map(lambda x:x[0], flist))))


with open('user-tweet-similar.json','w')as jj:
    json.dump(d,jj)

