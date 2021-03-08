import time
from anagrams.anagrams import system_dict, alphabetise_dictionary


# Legible
def match_word_in_alphabetised_dict(word: str, alphabetised_dict: dict):
    """
    Given a work and a dictionary organised as a tree,
    can we find the word in the dictionary,
    and return the remaining branch?
    """
    _current_dict_ = alphabetised_dict
    if len(word) == 0:
        return _current_dict_
    else:
        i = word[0]
        if i in _current_dict_.keys():
            _current_dict_ = _current_dict_[i]
            return match_word_in_alphabetised_dict(word[1:], _current_dict_)


def match_two_alphabetised_dict(dict_1: dict, dict_2: dict):
    """
    Given two dictionaries organised as trees,
    can we find whether they have any matches
    and return them as a list of strings?
    """
    if dict_1 is None or dict_2 is None:
        pass
    elif dict_1 == {"#": {}} and dict_2 == {"#": {}}:
        return ['']
    else:
        output = []
        for k in dict_1.keys():
            if k in dict_2.keys():
                match = match_two_alphabetised_dict(dict_1[k], dict_2[k])
                if match is None:
                    pass
                else:
                    output.extend([k+_str_ for _str_ in match])
                    return output


def find_concatenated_words_legible(short_dict: dict, long_dict: dict):
    output = []
    for word in short_dict:
        left_over = match_word_in_alphabetised_dict(word, long_dict)
        match = match_two_alphabetised_dict(left_over, short_dict)
        if match is not None:
            output.extend([(word, _str_) for _str_ in match])
    return output


# Fast
def match_two_dict(dict_1: dict, dict_2: dict):
    """
    Given two dictionaries organised as trees,
    can we find whether they have any matches, with branches left on dict_2
    and return them as a dictionary:
    * keys being the string of common keys;
    * values being the remaining branch?
    """
    if dict_1 is None or dict_2 is None:
        pass
    # TODO: Also stop when there’s the end of a word
    elif dict_1 == {}:
        return {'': dict_2}
    else:
        output = {}
        for letter, branch in dict_1.items():
            if letter == '#':
                output.update({'': dict_2})
            elif letter in dict_2.keys():
                match = match_two_dict(branch, dict_2[letter])
                if match is None:
                    pass
                else:
                    output.update({(letter+k): v for k, v in match.items()})
        return output


def find_concatenated_words_fast(short_dict: dict, long_dict: dict):
    leftover = match_two_dict(short_dict, long_dict)
    output = []
    for k, v in leftover.items():
        match = match_two_dict(v, short_dict)
        exact_matches = [(k, kk) for kk, vv in match.items() if vv == {'#': {}}]
        if len(exact_matches) > 0:
            output.extend(exact_matches)
    return output


# Pooling
def process_dictionaries(long_dict=None, short_dict=None):
    # Build alphabetised dictionaries
    if long_dict is None:
        long_dict = [word for word in system_dict if len(word) == 6]
    if short_dict is None:
        short_dict = [word for word in system_dict if len(word) < 6]
    return alphabetise_dictionary(long_dict), alphabetise_dictionary(short_dict)


if __name__ == '__main__':
    # short_d = ['A', 'baris', 'a', 'based', 'Ab', 'eria']
    # long_d = ['Abaris', 'abased', 'Aberia']
    # long_dict, short_dict = process_dictionaries(long_d, short_d)

    long_dict, short_dict = process_dictionaries()

    start = time.perf_counter()
    output_fast = find_concatenated_words_fast(short_dict, long_dict)
    stop = time.perf_counter()
    print(stop - start)
    print(len(output_fast))
    print(output_fast)

    start = time.perf_counter()
    output_legible = find_concatenated_words_legible(short_dict, long_dict)
    stop = time.perf_counter()
    print(stop - start)
    print(len(output_legible))
    print(output_legible)
