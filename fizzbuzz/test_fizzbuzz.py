import unittest
import fizzbuzz


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(fizzbuzz.process(2), '2')
        self.assertEqual(fizzbuzz.process(5), 'Buzz')
        self.assertEqual(fizzbuzz.process(6), 'Fizz')
        self.assertEqual(fizzbuzz.process(7), '7')
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')
        self.assertEqual(fizzbuzz.process(35), 'Buzz')
        self.assertEqual(fizzbuzz.process(90), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
