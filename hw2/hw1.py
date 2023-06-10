"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    # read the text in the article. Further there are from lines of text a list of words.
    # based on a list of words, create an array of pairs (number of variable characters in a word, word)
    # sort the list by supply keys word length and number of characters to set
    sorted_arr = sorted(sorted([(len(set(word)), word) for word in open(file_path).read().split()], key=lambda x: len(x[1]))), 


def get_rarest_char(file_path: str) -> str:
    # read file into string 
    file_str = open(file_path).read()
    # get all the unique characters of the file
    symbols_arr = set(file_str)
    # sort the list of tuples (character, number of characters in the text) by number and return the first element
    return sorted([(symbol, file_str.count(symbol)) for symbol in symbols_arr], key=lambda x: x[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    return sum([open(file_path).read().count(symb) for symb in ['.', ',', '!', '?', ';', ':']])


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
 f = 5 


