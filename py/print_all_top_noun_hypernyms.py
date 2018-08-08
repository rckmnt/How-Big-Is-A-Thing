# print all top hypernyms of nouns
# https://stackoverflow.com/questions/36060492/nltk-wordnet-verb-hierarchy

from nltk.corpus import wordnet as wn
from itertools import chain
from collections import Counter

wn.synsets('car')[0].root_hypernyms()

wn.synsets('love')[0].root_hypernyms()

wn.synsets('love', 'v')[0].root_hypernyms()

#It seems that there's no overarching/umbrella hypernym that covers all verbs, unlike nouns that covered by entity.n.01:

root_hypernyms_of_nouns = Counter(chain(*[ss.root_hypernyms() for ss in wn.all_synsets(pos='n')]))
len(root_hypernyms_of_nouns)

print(root_hypernyms_of_nouns.items())
# [(Synset('entity.n.01'), 82115)]
# [Finished in 19.0s]

