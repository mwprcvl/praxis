#!/usr/bin/env/python3

"""
Given a string s consisting of words and spaces, return the length of the last
 word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(s.strip(' ').split(' ')[-1])
    def solve(self, string: str) -> int:
        res = 0
        for char in string[::-1]:
            if char != ' ':
                res += 1
            elif res:
                return res
        return res


sol = Solution()

assert sol.solve("Hello World") == 5
assert sol.solve("   fly me   to   the moon  ") == 4
assert sol.solve("luffy is still joyboy") == 6
