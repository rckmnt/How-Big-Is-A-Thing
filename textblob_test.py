# textblob
from textblob import Word

blahs = ['golden_retriever', 'greenhouse', 'polo_mallet', 'paperboy',
        'pluto', 'quartzffsite', 'powder_keg','power_drill']


for b in blahs:
    word = Word(b)
    if word.synsets:
        plant = word.synsets[0]
        print('{} exists: {}'.format(b, word.synsets))
        print('\t\t {}'.format(plant.hypernyms()))
    else:
        print('{} is not a word'.format(b))


"""
print(word.synsets[:5])
print(word.definitions[:5])
plant = word.synsets[1]
print(plant.hypernyms())
print(plant.lemma_names)
print(plant.hypernyms())
print(plant.hyponyms()[:3])
print(plant.member_holonyms())
print(plant.part_meronyms())
"""
