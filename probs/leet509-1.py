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

    def solve(self, n: int) -> int:
        """ """
        if n == 0 or n == 1:
            return n
        fm0, fm1 = 1, 0
        for _ in range(n - 1):
            fm0, fm1 = fm0 + fm1, fm0
        return fm0


sol = Solution()

assert sol.solve(2) == 1
assert sol.solve(3) == 2
assert sol.solve(4) == 3
print(sol.solve(10))
