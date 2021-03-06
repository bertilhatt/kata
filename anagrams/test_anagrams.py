import unittest
from anagrams import anagrams


class MyTestCase(unittest.TestCase):
    def test_list_of_list(self):
        anagram_list_of_list = [
            ['enlist', 'nestli', 'lentis', 'lintse', 'listen', 'instel',
             'setlin', 'silent', 'tensil', 'tinsel'],
            ['crepitus', 'putresci', 'pictures', 'piecrust'],
            ['paste', 'pates', 'peats', 'septa', 'spate', 'tapes', 'stepa',
             'asept', 'steap', 'espat', 'petas', 'apest', 'peast', 'teasp',
             'stape']
        ]
        for _list_ in anagram_list_of_list:
            self.assertEqual(set(anagrams(_list_[0])), set(_list_))


if __name__ == '__main__':
    unittest.main()
