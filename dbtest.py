__author__ = 'mojtaba'
import gensim
from gensim.models import doc2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model1 = Doc2Vec.load('golduser.model')
model1.init_sims(replace=True)
print model1.docvecs.most_similar(931826418)


