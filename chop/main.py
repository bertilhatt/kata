#!/usr/bin/env python3

# [ ] traditional iterative approach
# [x] one might be recursive,
# [ ] one might use a functional style passing array slices

class Chop:
    def __init__(self, search_term: int, lst: list):
        self.search_term = search_term
        self.lst = lst

    def slice(self, m: int, n: int):
        if m == n:
            return -1
        elif m + 1 == n:
            if self.lst[m] == self.search_term:
                return m
            else:
                return -1
        else:
            i = (m + n) // 2
            if self.lst[i] <= self.search_term:
                pos = self.slice(i, n)
            else:
                pos = self.slice(m, i)
            return pos


def chop_recursive(search_term: int, lst: list):
    """Recursive"""
    if len(lst) == 0:
        return -1
    if len(lst) == 1:
        return 0 if search_term == lst[0] else -1
    else:
        m = len(lst) // 2
        if search_term < lst[m]:
            pos = chop_recursive(search_term, lst[:m])
        else:
            half_pos = chop_recursive(search_term, lst[m:])
            if half_pos >= 0:
                pos = m + half_pos
            else:
                pos = -1
    return pos


# chop = chop_recursive
def chop(search_term: int, lst: list):
    chop_instance = Chop(search_term, lst)
    return chop_instance.slice(0, len(lst))


if __name__ == '__main__':
    print('PyCharm')
