#!/usr/bin/env/python3

"""
Given an integer array nums and an integer val, remove all occurrences of val in
 nums in-place. The order of the elements may be changed. Then return the number
 of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get
 accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements
 which are not equal to val. The remaining elements of nums are not important as
 well as the size of nums.

Return k.
"""


class Solution:
    """ """

    def removeElement(self, nums: list[int], val: int) -> int:
        """ """

        found_idxs = []
        
        for idx, ele in enumerate(nums):

            if nums[idx] == val:
                found_idxs.append(idx)
        k = len(found_idxs)
        import pdb;pdb.set_trace()

        tail_idx = len(nums) - 1
        while found_idxs:
            if nums[tail_idx] == val:
                found_idxs.pop(-1)
                nums[tail_idx] = -1
            else:
                found_idx = found_idxs.pop(0)
                nums[found_idx], nums[tail_idx] = nums[tail_idx], -1
            tail_idx -= 1

        import pdb;pdb.set_trace()

        return len(nums) - k


sol = Solution()

nums = [3,2,2,3]
assert sol.removeElement(nums, 3) == 2
assert nums[:2] == [2, 2]

nums = [0,1,2,2,3,0,4,2]
assert sol.removeElement(nums, 2) == 4
assert nums[:5] == [0,1,4,0,3]
