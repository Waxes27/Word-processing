import re
import string
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
    """
    creates a list from a sentence
    """
    text = text.lower()
    word_list = split("?,.; ",text)
    #print(len(word_list[0]))
    for i in word_list:
        [word_list.remove(i) for i in word_list if len(i) == 0]
    return word_list


def words_longer_than(length, text):
    """
    finds words longer than specified arg...
    """
    word_list = split("?,.; ",text)
   
    return [i for i in word_list if len(i) > length]


def words_lengths_map(text):
    """
    mapping len of word : number of those words
    """
    length_of_words = []
    text = convert_to_word_list(text)
    [length_of_words.append(len(i)) for i in text]
    dictionary = {length_of_word: length_of_words.count(length_of_word) for length_of_word in sorted(length_of_words)}
    # a = tuple(map(lambda word: len(word),text))# LAMBDA VERSION with MAP
    return dictionary#dict(sorted(dictionary.items(), key = lambda kv: (kv[1], kv[0])))


def get_alphabet_characters():
    """
    returns list of alphabets
    """
    return list(string.ascii_lowercase)


def letters_count_map(text):
    """
    return a dict() with an index of the letters found in the text param
    """
    alpha = get_alphabet_characters()
    text = convert_to_word_list(text)
    list_of_chars = []
    for x in range(len(text)):
        [list_of_chars.append(i) for i in text[x]]
    dictionary = {alpha:list_of_chars.count(alpha) for alpha in alpha}
    return dictionary


def most_used_character(text):
    """
    finds the most used character
    """
    list_of_chars= []
    alpha = get_alphabet_characters()
    for x in range(len(text)):
        [list_of_chars.append(i) for i in text[x]]
    dictionary = {list_of_chars.count(alpha):alpha for alpha in alpha}
    dictionary = sorted(dictionary.items())
    if len(dictionary) != 1:
        return dictionary.pop(-1)[1]
    else:
        return


#print(words_lengths_map("Facing his greatest fear, he ate his first marshmallow."))