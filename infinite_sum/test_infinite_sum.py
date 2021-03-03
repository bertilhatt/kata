import unittest
from math import fabs
from infinite_sum import solve


class MyTestCase(unittest.TestCase):
    def assert_fuzzy(self, m, expect):
        max_error = 1e-12
        s = '{:.2f}'.format(m)
        actual = solve(m)
        in_range = fabs(actual - expect) <= max_error
        if not in_range:
            msg = f"Expected value near {expect:.12e} but got {actual:.12e}"
            print(msg)
        self.assertTrue(in_range, f'Error in solve({m})')

    def test_basics(self):
        self.assert_fuzzy(2.00, 5.000000000000e-01)
        self.assert_fuzzy(4.00, 6.096117967978e-01)
        self.assert_fuzzy(5.00, 6.417424305044e-01)
        self.assert_fuzzy(6.00, 6.666666666667e-01)
