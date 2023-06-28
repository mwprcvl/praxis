#!/usr/bin/env/python3

"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:

    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) == str(x)[::-1]:
            return True
        return False


sol = Solution()

assert sol.is_palindrome(121) == True
assert sol.is_palindrome(-121) == False
assert sol.is_palindrome(10) == False
