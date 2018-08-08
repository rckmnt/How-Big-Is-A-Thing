"""
coding: utf-8

About:
    This module does the NLP algorithm of looking up How Big something is.
    It calls a dataset "corpus.csv" and textblob.


Attributes:
    # Use textblob to get hypernyms from wordnet
    # https://stevenloria.com/wordnet-tutorial/

Todo:
    # TODO - add a kwargs for Original word so it'll get passed thru to print
    # TODO - OR add a nested func for the counter parameter

Author: Scott Leinweber, 2018
Support: Studio for Creative Inquiry, CMU
"""

from textblob import Word


# Write a function that will get a noun's hypernym:

def get_hypernym(askedfor):
    # put in a word, get a list of other words
    word = Word(askedfor)
    if word.synsets:
        generalsenses = word.synsets[0]
        next_level = [h.name().split(".")[0] for h in  generalsenses.hypernyms()]
        print('A {} is a/an {}'.format(askedfor, next_level[0]))
        return(next_level[0])
    else:
        print('{} is NOT a word'.format(askedfor))
        return('{} is NOT a word'.format(askedfor))


# Some basic test word lists:

test_words = ["pool", "sushi", "dog", "sddfds", "shame", "pickup_truck", "african_leopard", "mailbox"]
test_words_2 = ["bug", "fox", "salad", "chair", "table", "nintendo", "trash_can"]


# for t in test_words:
#     get_hypernym(t)


# Import my edited MTurk'd corpus of ~1200 words and sizes

import csv

corpus_sizes = {}

with open('corpus.csv', 'rU') as csvfile:
    readCSV = csv.reader(csvfile, dialect=csv)
    for row in readCSV:
        corpus_sizes[row[0].lower()] = row[1]
#         print(row[0].lower(), row[1])

# When using plaintext file use delimiter='\t' to read


# Create basic dictionary of the 10 bins and corresponding sizes.

binned_sizes = {
    1 : "Insect ~ 5mm",
    2 : "Thumbnail ~ 20mm",
    3 : "Index Finger ~ 80mm",
    4 : "Hand, a fist, a baseball ~ 150mm",
    5 : "Loaf of bread or a cat ~ 300mm",
    6 : "Full arm length ~ 1m",
    7 : "Adult person ~ 2.5m",
    8 : "Car ~ 4m",
    9 : "House or a large Tree ~ 10m",
    10 :" Football field ~ 50m+",
}



nums = [1,3,10,29,7,5]

def is_num_a_size(num):
    if n in binned_sizes:
        print("{} is about the size of a/an {}".format(n, binned_sizes[n]))
        return(n)
    else:
        print("{} is not in binned_sizes".format(n))

# print([is_num_a_size(n) for n in nums])


# Write functions to get either the bin number or description of a noun string


def get_num_size_from_corpus(askword):
    print(corpus_sizes[askword])
    return(corpus_sizes[askword])

def get_desc_size_from_corpus(original_word, askword):
    num_size = corpus_sizes[askword]
    msg = binned_sizes[int(num_size)].lower()
    print("A {} is about the size of a {}.".format(original_word, msg))

# get_num_size_from_corpus('dog')
# get_desc_size_from_corpus('golden_retriever', 'dog')



def is_hypernym_in_corpus(askedfor):
    # put in a word, get a list of other words
    word = Word(askedfor)
    if word.synsets:
        generalsenses = word.synsets[0]
        next_level = [h.name().split(".")[0] for h in  generalsenses.hypernyms()]
        if next_level[0] in corpus_sizes:
            print('{} >>> {}'.format(askedfor, next_level[0]))
            print(get_desc_size_from_corpus(askedfor, next_level[0]))
            print('\n')
            return(next_level)
        else:
            print('A {} is a "{}"'.format(askedfor, next_level[0]))
            print('But hypernym "{}" is not in corpus'.format(next_level[0]))
    else:
        print('{} does not have synsets.'.format(askedfor))
        return(False)



# for t in test_words_2:
#     is_hypernym_in_corpus(t)


# is_hypernym_in_corpus("flamingo")
# is_hypernym_in_corpus("scottish_terrier")
# is_hypernym_in_corpus("digital_computer")
# is_hypernym_in_corpus("edible_fruit")


def how_big_is_a(askedfor, counter):
    # recurse_is_hypernym_in_corpus def
    # put in a word, get a list of other words
    # TODO - add a kwargs for Original word so it'll get passed thru to print
    # TODO - OR add a nested func for the counter parameter

    firstquery = askedfor
    word = Word(askedfor)
    print("A {} is a...".format(firstquery))
    if word.synsets:
        generalsenses = word.synsets[0]
        next_level = [h.name().split(".")[0] for h in  generalsenses.hypernyms()]
        if next_level[0] in corpus_sizes:
            print('\n{} >>> {}\n'.format(firstquery, next_level[0]))
            print(get_desc_size_from_corpus(askedfor, next_level[0]))
            print('\n')
            return(next_level)
            counter = counter + 1

        elif counter < 5:
            counter = counter + 1
            how_big_is_a(next_level[0], counter)
            return(next_level[0])

        else:
            print('A {} is a "{}"'.format(askedfor, next_level[0]))
            print('But hypernym "{}" is not in corpus'.format(next_level[0]))
            return(False)
    else:
        print('{} does not have synsets.'.format(askedfor))
        return(False)



# how_big_is_a("headache", 0)
# how_big_is_a("sandwich", 0)




"""
def opt_fun(x1, x2, *positional_parameters, **keyword_parameters):
...     if ('optional' in keyword_parameters):
...         print 'optional parameter found, it is ', keyword_parameters['optional']
...     else:
...         print 'no optional parameter, sorry'
"""

# TODO - idk how kwargs work but maybe put in one for the original
#        as it loops recursively it keeps the original one.

# another method could be nested defs
# def general(whatever)
#     orignal word = whatever
#     def recursiveonehere()
#         do recurse
#     return orignal + recurse size

"""
def recurse_kwargs_is_hypernym_in_corpus(askedfor, *original):
    # put in a word, get a list of other words
    counter = 0
    firstquery = askedfor
    word = Word(askedfor)
    if word.synsets:
        generalsenses = word.synsets[0]
        next_level = [h.name().split(".")[0] for h in  generalsenses.hypernyms()]
        if next_level[0] in corpus_sizes:
            print('{} >>> {}'.format(firstquery, next_level[0]))
            print(get_desc_size_from_corpus(askedfor, next_level[0]))
            print('\n')
            return(next_level)
        elif counter < 5:
            recurse_is_hypernym_in_corpus(next_level[0], firstquery)
            counter += 1
            return(next_level[0])
        else:
            print('A {} is a "{}"'.format(askedfor, next_level[0]))
            print('But hypernym "{}" is not in corpus'.format(next_level[0]))
            return(False)
    else:
        print('{} does not have synsets.'.format(askedfor))
        return(False)

"""





# recurse_kwargs_is_hypernym_in_corpus("boston_terrier")

