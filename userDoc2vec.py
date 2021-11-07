__author__ = 'mojtaba'
import logging
import ast
from gensim.models.doc2vec import Doc2Vec, TaggedDocument,utils


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
class TaggedLineDocument(object):
    """Simple format: one document = one line = one TaggedDocument object.
    Words are expected to be already preprocessed and separated by whitespace,
    tags are constructed automatically from the document line number."""
    def __init__(self, UsersData):
        """
        `source` can be either a string (filename) or a file object.
        Example::
            documents = TaggedLineDocument('myfile.txt')
        Or for compressed files::
            documents = TaggedLineDocument('compressed_text.txt.bz2')
            documents = TaggedLineDocument('compressed_text.txt.gz')
        """
        self.source = UsersData

    def __iter__(self):
        """Iterate through the lines in the source."""
        try:
            # Assume it is a file-like object and try treating it as such
            # Things that don't have seek will trigger an exception
            self.source.seek(0)
            for item_no, line in enumerate(self.source):
                yield TaggedDocument(utils.to_unicode(line).split(), [item_no])
        except AttributeError:
            # If it didn't work like a file, use it as a string filename
            with utils.smart_open(self.source) as fin:
                for line in fin:
                    sentence=ast.literal_eval(line)
                    id=sentence[0]
                    tweet =(sentence[1])
               # for item_no, line in enumerate(fin):
                    yield TaggedDocument(utils.simple_preprocess(' '.join(tweet)),(id))
# sentences=doc2vec.TaggedLineDocument('G:\NewsData')
document = TaggedLineDocument('UsersData')
model = Doc2Vec(document, size=35 , window=5, min_count=2, workers=4,iter=25,dm=0,hs=1)
#model.build_vocab(document)
#model.train(document)
model.save('userDoc.model')






