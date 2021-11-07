__author__ = 'mojtaba'
import logging
import os
import json
import collections
import random
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def read_corpus():
    f = open('data.json')
    g = f.read()
    data = json.loads(g)
    for key in data:
        yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(' '.join(data[key])),(key.strip()))
train_corpus = list(read_corpus())
#print train_corpus[:2]
model = gensim.models.doc2vec.Doc2Vec(train_corpus,size=50,window=5, min_count=2, iter=30)
#model.build_vocab(train_corpus)
#model.train(train_corpus)
model.save('juser.model')


