#!/usr/bin/env/python3

"""
Given a sorted array of distinct integers and a target value, return the index
 if the target is found. If not, return the index where it would be if it were
 inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    """ """

    def solve(self, nums: list[int], target: int) -> int:
        """ """
        low = 0
        mid = len(nums) // 2
        upp = len(nums) - 1
        import pdb;pdb.set_trace()
        if not nums:
            return 0
    
        if nums[low] == target:
            return low
        
        if nums[mid] > target:
            return self.solve(nums[:mid], target)
        
        if nums[mid] == target:
            return mid

        if nums[upp] > target:
            return mid + 1 + self.solve(nums[mid + 1:], target)
        
        if nums[upp] == target:
            return upp
        
        if nums[upp] < target:
            return upp + 1


sol = Solution()

# assert sol.solve([], 4) == 0
# assert sol.solve([1,3,5,6], 5) == 2
# assert sol.solve([1,3,5,6], 2) == 1
# assert sol.solve([1,3,5,6], 7) == 4
assert sol.solve([1,3,5], 4) == 2
