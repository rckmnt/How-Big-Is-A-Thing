# word2vec attempts

# http://textminingonline.com/getting-started-with-word2vec-and-glove-in-python

from gensim.models import word2vec

# sentences = word2vec.Text8Corpus('text8')

# import modules and set up logging

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# load up unzipped corpus from http://mattmahoney.net/dc/text8.zip
sentences = word2vec.Text8Corpus('text8')

# train the skip-gram model; default window=5
model = word2vec.Word2Vec(sentences, size=200)

# ... and some hours later... just as advertised...
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)[('queen', 0.5359965)]


# model_org = word2vec.Word2Vec.load_word2vec_format('vectors.bin', binary=True)

# print(model_org.most_similar('frog'))