# pylint: disable-all
import unittest
from typing import List
"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums)+1):
            if i in nums:
                continue
            else:
                result.append(i)
        return result

    def findDisappearedNumbers_better(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual([5, 6], solution.findDisappearedNumbers_better(nums=[4, 3, 2, 7, 8, 2, 3, 1]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual([2], solution.findDisappearedNumbers_better(nums=[1, 1]))

    def test_example3(self):
        solution = Solution()
        self.assertEqual([5, 6], solution.findDisappearedNumbers_better(nums=[4,3,2,7,8,2,3,1]))

if __name__ == '__main__':
    unittest.main()
