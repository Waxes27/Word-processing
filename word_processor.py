import re
import time
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    text = text.lower()
    word_list = split("?,.; ",text)
    #print(len(word_list[0]))
    for i in word_list:
        [word_list.remove(i) for i in word_list if len(i) == 0]
    return word_list


def words_longer_than(length, text):
    word_list = split("?,.; ",text)
   
    return [i for i in word_list if len(i) > length]


def words_lengths_map(text):
    """
    mapping len of word : number of those words
    """
    word_list = convert_to_word_list(text)
    
    dictionary = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 14:0}
    for i in word_list:
        if int(len(i)) in dictionary:
            dictionary[int(len(i))] += 1
    values = list(dictionary.values())
    print(values)
    for i in values:
        if i == 0:
            values.remove(i)
    print(values)


    return dictionary

def letters_count_map(text):
    pass


def most_used_character(text):
    pass

print(words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?'))
