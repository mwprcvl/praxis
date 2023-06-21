#!/usr/bin/env/python3

"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    """ recursive edition """

    def reverse_it(self, num: int, rev: int) -> int:
        if not num:
            return rev
        num, rem = divmod(num, 10)
        return self.reverse_it(num, rev * 10 + rem)
    
    def is_palindrome(self, num: int) -> bool:
        if num < 0:
            return False
        rev = self.reverse_it(num, 0)
        return True if rev == num else False


sol = Solution()

assert sol.is_palindrome(121) == True
assert sol.is_palindrome(-121) == False
assert sol.is_palindrome(10) == False
