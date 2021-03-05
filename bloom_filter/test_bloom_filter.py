import unittest
from bloom_filter import Bouquet


class MyTestCase(unittest.TestCase):
    def test_consistency(self):
        bouquet = Bouquet(hash_num=5, bitmap_size=4)
        test_dict = ['abc', 'cbd', 'edf', 'fgh']
        bouquet.fill(test_dict)
        for _str_ in test_dict:
            self.assertTrue(bouquet.check_presence(_str_))

    def test_efficacy(self):
        bouquet = Bouquet(hash_num=5, bitmap_size=4)
        test_dict = ['abc', 'cbd', 'edf', 'fgh']
        other_dict = ['clk', 'rds', 'dgh', 'fhi']
        bouquet.fill(test_dict)
        for _str_ in other_dict:
            self.assertFalse(bouquet.check_presence(_str_))


if __name__ == '__main__':
    unittest.main()
