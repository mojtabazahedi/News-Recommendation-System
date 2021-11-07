import gensim
import os
import collections
import random
import io
import json
import logging
#########
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def wvj():
    train_file =r'G:\twitter\Twitter\gold.json'
    f = open(train_file)
    jj = json.loads(f.read())

    for key in jj:
     yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(' '.join(jj[key])), [str(key).lstrip()])

train_corpus = list(wvj())

model = gensim.models.Doc2Vec(size=400 , window=10, min_count=2, workers=4,iter=20,dm=0,hs=1)
model.build_vocab(train_corpus)
model.train(train_corpus)
model.save('golduser.model')






