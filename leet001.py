#!/usr/bin/env/python3

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        dct = {}
        for idx, ele in enumerate(nums):
            rem = target - ele
            if rem in dct:
                return [dct[rem], idx]
            dct[ele] = idx


sol = Solution()

assert sol.two_sum([2,7,11,15], 9) == [0,1]
assert sol.two_sum([3,2,4], 6) == [1,2]
assert sol.two_sum([3,3], 6) == [0,1]
