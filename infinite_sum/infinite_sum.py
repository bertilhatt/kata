#!/usr/bin/env python3

from math import fabs


def solve(m: float):
    epsilon = 1e-12
    lo, hi = 0, 1
    inf_sum = -1
    while fabs(inf_sum - m) >= epsilon:
        x = (lo + hi) / 2
        inf_sum = 0
        i = 1
        while i * x**i > epsilon and inf_sum < m + epsilon:
            inf_sum += i * x**i
            i += 1
        if inf_sum > m + epsilon:
            hi = x
        elif inf_sum < m - epsilon:
            lo = x
    return x


if __name__ == '__main__':
    m = input("What infinite sum do you want to find?")
    try:
        m = float(m)
        if m > 0:
            print(solve(m))
    except ValueError:
        print("Try a positive number")
    pass
