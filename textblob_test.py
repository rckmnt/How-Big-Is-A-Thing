# textblob
from textblob import Word

blahs = ['golden_retriever', 'greenhouse', 'polo_mallet', 'paperboy',
        'pluto', 'quartzffsite', 'powder_keg','power_drill']


# for b in blahs:
#     word = Word(b)
#     if word.synsets:
#         plant = word.synsets[0]
#         print('{} exists: {}'.format(b, word.synsets))
#         print('\t\t {}'.format(plant.hypernyms()))
#     else:
#         print('{} is NOT a word'.format(b))


def get_hypernym(askedfor):
    # put in a word, get a list of other words
    word = Word(askedfor)
    if word.synsets:
        plant = word.synsets[0]
        plainword = [h.name().split(".")[0] for h in  plant.hypernyms()]
        print('A {} is a/an {}'.format(askedfor, plainword[0]))
        return(plainword)
    else:
        print('{} is NOT a word'.format(askedfor))
        return('{} is NOT a word'.format(askedfor))

get_hypernym("pool")
get_hypernym("sushi")
get_hypernym("sddfds")
get_hypernym("shame")
get_hypernym("pickup_truck")
get_hypernym("african_leopard")
get_hypernym("mailbox")



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
