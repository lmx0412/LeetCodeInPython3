# pylint: disable-all
import unittest
from typing import List
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0, 0]
        if nums[0] != 1:
            result[1] = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                result[0] = nums[i]
                continue
            if nums[i + 1] != nums[i] + 1:
                result[1] = nums[i] + 1
        if result[1] == 0:
            result[1] = nums[-1] + 1
        return result

    def findErrorNums_oneline(self, nums):
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))]

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual([2, 3], solution.findErrorNums(nums=[1, 2, 2, 4]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual([1, 2], solution.findErrorNums(nums=[1, 1]))

    def test_example3(self):
        solution = Solution()
        self.assertEqual([7, 8], solution.findErrorNums(nums=[1, 2, 3, 4, 5, 6, 7, 7]))

    def test_example4(self):
        solution = Solution()
        self.assertEqual([2, 1], solution.findErrorNums(nums=[2, 2]))

    def test_example5(self):
        solution = Solution()
        self.assertEqual([2, 1], solution.findErrorNums(nums=[2, 3, 2]))

    def test_example6(self):
        solution = Solution()
        self.assertEqual([2, 10], solution.findErrorNums(nums=[1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))


if __name__ == '__main__':
    unittest.main()
