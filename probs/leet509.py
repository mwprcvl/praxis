#!/usr/bin/env/python3

"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
 Fibonacci sequence, such that each number is the sum of the two preceding
 ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


class Solution:
    """ """

    def recur(self, n_1: int, n_2: int, n: int) -> int:
        """ """
        n_0 = n_1 + n_2
        if n == 2:
            return n_0
        return self.recur(n_0, n_1, n - 1)

    def solve(self, n: int) -> int:
        """ """
        if n == 0 or n == 1:
            return n
        return self.recur(1, 0, n)


sol = Solution()

assert sol.solve(2) == 1
assert sol.solve(3) == 2
assert sol.solve(4) == 3
