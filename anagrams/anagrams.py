
import os
import sys
from collections import Counter

system_dict_path = '/usr/share/dict/words'
with open(system_dict_path, 'r') as f:
    system_dict = f.read().split('\n')


def alphabetise_dictionary(word_dict=None):
    if word_dict is None:
        word_dict = system_dict
    output_dict = {}
    for _word_ in word_dict:
        _dict_ = output_dict
        for letter in _word_+'#':
            if letter not in _dict_.keys():
                _dict_[letter] = {}
            else:
                pass
            _dict_ = _dict_[letter]
    return output_dict


alphabetised_dictionary = alphabetise_dictionary()


def find_word(letter_counter, dict_tree=None):
    if dict_tree is None:
        dict_tree = alphabetised_dictionary
    _current_tree_ = dict_tree
    output = []
    if max(letter_counter.values()) <= 0:
        return ['']
    for k in letter_counter:
        if k in _current_tree_.keys() and letter_counter[k] > 0:
            _letter_counter_ = letter_counter.copy()
            _letter_counter_[k] -= 1
            list_rest = find_word(_letter_counter_, dict_tree=_current_tree_[k])
            if list_rest is not None and list_rest != []:
                output.extend([k+rest for rest in list_rest])
    return output


def anagrams(suggestion, word_dict=None):
    return find_word(Counter(suggestion), dict_tree=word_dict)


if __name__ == '__main__':
    with open('input_words', 'r') as file:
        word_list = file.read().splitlines()

    for word in word_list:
        print(' '.join(anagrams(word)))
