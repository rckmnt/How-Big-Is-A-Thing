# import nltk
# nltk.download()

from nltk.corpus import wordnet as wn

words = {
    'golden_retriever' : 1,
    'greenhouse' : 7,
    'polo_mallet' : 3,
    'paperboy' : 2,
    'pluto': 10,
    'quartzsite': 1,
    'powder_keg': 5,
    'power_drill': 7
}

# for k in words:
#     print(wn.synsets(k))
    # print(wn.sens(k))

# all nouns
# wordnet.synsets(word, pos='n')
"""
for synset in wn.synsets('can'):
   print(synset.lexname)
   print(synset.hypernyms())
   print(synset.root_hypernyms())
   print(wn.synset('can').root_hypernyms())

for synset in wn.synsets('dalmatian'):
   print(synset)

for synset in wn.synsets('poodle').hypernyms:
   print(synset.lexname)
"""

# https://stevenloria.com/wordnet-tutorial/
from textblob import Word

word = Word("dalmatian")

print(word.synsets[:5])

print(word.definitions[:5])

plant = word.synsets[1]

print(plant.lemma_names)

print('\n')

print(plant.hypernyms())

print(plant.hyponyms()[:3])

print(plant.member_holonyms())

print(plant.part_meronyms())


# dags = ['poodle', 'dalmatian', 'schnauzer', 'bulldog']

# for d in dags:
#     word = Word(d)
#     plant = word.synsets[0]
#     print(plant.hypernyms())


# https://stackoverflow.com/questions/1695971/does-wordnet-have-levels-nlp#1695983

# nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}


# for n in sorted(nouns):
#     print(unicode(n))
