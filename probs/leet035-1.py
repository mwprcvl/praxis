#!/usr/bin/env/python3

"""
Given a sorted array of distinct integers and a target value, return the index
 if the target is found. If not, return the index where it would be if it were
 inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

import bisect


class Solution:
    """ """

    def solve(self, nums: list[int], target: int) -> int:
        """ """
        if not nums:
            return 0
        return bisect.bisect_left(nums, target)


sol = Solution()

assert sol.solve([], 4) == 0
assert sol.solve([1,3,5,6], 5) == 2
assert sol.solve([1,3,5,6], 2) == 1
assert sol.solve([1,3,5,6], 7) == 4
assert sol.solve([1,3,5], 4) == 2
