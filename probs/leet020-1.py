#!/usr/bin/env/python3

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution():
    """ """

    def solve(self, brs: str) -> bool:
        """ """
        lkp = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in brs:
            if char in lkp:
                stack.append(char)
                continue
            if stack and (char == lkp[stack[-1]]):
                stack.pop()
                continue
            return False
        return False if stack else True


sol = Solution()

assert sol.solve('()') is True
assert sol.solve('()[]{}') is True
assert sol.solve('(]') is False
