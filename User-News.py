__author__ = 'mojtaba'
import gensim
from gensim.models import doc2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import logging
import ast

t=open('UsersData','r')
for line in t:
        sentence=ast.literal_eval(line)
        id=sentence[0]
        tweet =(sentence[1])
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model1 = Doc2Vec.load('news2vec.model')
model1.init_sims(replace=False)
st = str(sentence)

new_doc_vec = model1.infer_vector(st)

print model1.docvecs.most_similar([new_doc_vec])


