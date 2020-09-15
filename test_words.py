import unittest
import word_processor
from unittest.mock import patch
import string


text = "Facing his greatest fear, he ate his first marshmallow."
my_String = ['facing', 'his', 'greatest', 'fear', 'he', 'ate' ,'his', 'first', 'marshmallow']


class TestClass(unittest.TestCase):
    def test_convert_word_list(self):
        result = word_processor.convert_to_word_list(text)
        self.assertEqual(my_String, result)
    

    def test_words_longer_than(self):
        number = word_processor.words_longer_than(5,text)
        self.assertEqual(number,['Facing', 'greatest', 'marshmallow'])

        number = word_processor.words_longer_than(0,text)
        self.assertEqual(number, ['Facing', 'his', 'greatest', 'fear', 'he', 'ate','his', 'first', 'marshmallow'])


    def test_get_alpha(self):

        alpha = list(string.ascii_lowercase)
        alphabet = word_processor.get_alphabet_characters()
        self.assertEqual(alpha,alphabet)


    def test_words_lengths_map(self):
        texts = "You're good at English when you know the difference between a man eating chicken and a man-eating chicken."
        dictionary = {2: 1, 3: 3, 4: 1, 5: 1, 6: 1, 8: 1, 11: 1}
        result = word_processor.words_lengths_map(text)
        self.assertEqual(dictionary,result)

        dictionary = {1: 2, 2: 1, 3: 4, 4: 3, 6: 2, 7: 4, 10: 2}
        result = word_processor.words_lengths_map(texts)
        self.assertEqual(dictionary, result)



    def test_most_used_character(self):
        most_used_char = word_processor.most_used_character(text)
        self.assertEqual("a", most_used_char)
        self.assertEqual(None,word_processor.most_used_character(""))


    def test_letters_count_map(self):
        result = word_processor.letters_count_map(text)
        self.assertEqual(result,{'a': 6, 'b': 0, 'c': 1, 'd': 0, 'e': 5, 'f': 3, 'g': 2, 'h': 4, 'i': 4, 'j': 0, 'k': 0, 'l': 2, 'm': 2, 'n': 1, 'o': 1, 'p': 0, 'q': 0, 'r': 4, 's': 5, 't': 4, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 0, 'z': 0})



if __name__ == '__main__':
    unittest.main()
