# -*- coding: utf-8 -*-
"""
description:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
examples:    
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
nums = [3, 2, 3]
target = 6
nums = [3, 3]
target = 6

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            tmp = nums.copy()
            tmp.pop(i)
            if (target - nums[i]) in tmp:
                return [i, tmp.index(target - nums[i]) + 1]
        return [0, 0]


def main():
    solution = Solution()
    ret = solution.twoSum(nums, target)
    print(ret)

if __name__ == "__main__":
    main()