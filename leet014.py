#!/usr/bin/env/python3

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:

    def solve(self, words: list[str]) -> str:
        prefix = ''
        for idx, letter in enumerate(words[0]):
            for word in words[1:]:
                if idx == len(word):
                    return prefix
                if word[idx] != letter:
                    return prefix
            prefix += letter
        return prefix


sol = Solution()

assert sol.solve(['flower','flow','flight']) == 'fl'
assert sol.solve(['dog','racecar','car']) == ''
