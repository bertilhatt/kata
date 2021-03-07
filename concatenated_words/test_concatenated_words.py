import unittest
from contaneted_words_legible import find_concatenated_words


class MyTestCase(unittest.TestCase):
    def test_pairs(self):
        pairs = [['al', 'bums'], ['arm', 'ory'], ['ass', 'ume']]
        for pair in pairs:
            concat = ''.join(pair)
            output = find_concatenated_words([concat], pair)
            self.assertEqual([set(pairs)], output)


if __name__ == '__main__':
    unittest.main()
