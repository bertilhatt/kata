import time
from anagrams.anagrams import system_dict, alphabetise_dictionary




if __name__ == '__main__':
    start = time.perf_counter()
    answers = find_concatenated_words()
    stop = time.perf_counter()
    print(stop - start)
    print(len(answers))
    print(answers)
