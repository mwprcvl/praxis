#!/usr/bin/env/python3

"""
Given a string s consisting of words and spaces, return the length of the last
 word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    """ """

    def solve(self, string: str) -> int:
        """ """
        return len(string.strip(' ').split(' ')[-1])


sol = Solution()

assert sol.solve("Hello World") == 5
assert sol.solve("   fly me   to   the moon  ") == 4
assert sol.solve("luffy is still joyboy") == 6
