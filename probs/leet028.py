#!/usr/bin/env/python3

"""
Given two strings needle and haystack, return the index of the first occurrence
 of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # for idx, ele in enumerate(haystack):
        #     if idx + len(needle) > len(haystack):
        #         continue
        #     if haystack[idx:idx+len(needle)] == needle:
        #         return idx
        # return -1