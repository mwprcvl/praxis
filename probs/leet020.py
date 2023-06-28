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

    def find_close(self, brs: str) -> int:
        """ return the index of the closing bracket """
        lkp = {'(': ')', '{': '}', '[': ']'}
        open = brs[0]
        close = lkp[open]
        count = 1
        for idx in range(1, len(brs)):
            count += 1 if brs[idx] == open else 0
            count -= 1 if brs[idx] == close else 0
            # if match to open is found
            if not count:
                return idx
        # if close is not found
        return None


    def solve(self, brs: str) -> bool:
        """ """

        # base case when all brackets have been closed
        if not brs:
            return True
        # case when odd length must be bad brackets
        if len(brs) % 2:
            return False
        
        # case when first bracket is a close bracket
        if brs[0] in set([')', '}', ']']):
            return False
        # find the valid closing bracket index
        close_idx = self.find_close(brs)
        # case when close not found
        if not close_idx:
            return False

        # recursive case: split brs based upon valid close bracket index
        return all([self.solve(brs[1:close_idx]), self.solve(brs[close_idx + 1:])])


sol = Solution()

assert sol.find_close('(') is None
assert sol.find_close('()') == 1
assert sol.solve('()') is True
assert sol.solve('()[]{}') is True
assert sol.solve('(]') is False
