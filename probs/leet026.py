#!/usr/bin/env/python3

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates
 in-place such that each unique element appears only once. The relative order of
 the elements should be kept the same. Then return the number of unique elements
 in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need
 to do the following things:

Change the array nums such that the first k elements of nums contain the unique
 elements in the order they were present in nums initially. The remaining elements
 of nums are not important as well as the size of nums.

Return k.
"""


class Solution:
    """ """

    def remove_duplicates(self, nums: list[int]) -> int:
        """ """
        head, num = 0, -999
        for ele in nums:
            if ele != num:
                nums[head] = num = ele
                head += 1
        return head


sol = Solution()

nums = [1,1,2]
assert sol.remove_duplicates(nums) == 2
assert nums[:2] == [1,2]

nums = [0,0,1,1,1,2,2,3,3,4]
assert sol.remove_duplicates(nums) == 5
assert nums[:5] == [0,1,2,3,4]
