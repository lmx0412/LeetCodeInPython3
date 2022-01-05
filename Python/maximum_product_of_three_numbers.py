# pylint: disable-all
import unittest
from typing import List
"""

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return max(nums[0] * nums[1] * nums[2], nums[-1] * nums[-2] * nums[0])

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(6, solution.maximumProduct(nums=[3,2,1]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(24, solution.maximumProduct(nums=[1, 2, 3, 4]))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(-6, solution.maximumProduct(nums=[-1, -2, -3]))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(-6, solution.maximumProduct(nums=[-1, -2, -3, -4, -5]))


if __name__ == '__main__':
    unittest.main()
