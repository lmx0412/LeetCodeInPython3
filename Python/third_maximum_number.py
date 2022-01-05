# pylint: disable-all
import unittest
from typing import List
"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums: return
        nums = sorted(list(set(nums)), reverse=True)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]
    
    def thirdMax_better(self, nums: List[int]) -> int:
        
        '''
            Time complexity: O(n)
            Space complexity: O(1)
            
            Using a max heap of size 3 will result (log 3)*O(n), which is still O(n)
            However, Python has nlargsest() from heapq library instead of max heap
        '''
        
        nums = list(set(nums))  # 2*O(n)
        
        if len(nums) < 3:
            return max(nums)    # O(n)
        
        for i in range(2):      # 2*O(n)
            nums.remove(max(nums))
            
        return max(nums)        # O(n)


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(1, solution.thirdMax(nums=[3,2,1]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(2, solution.thirdMax(nums=[1, 2]))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(1, solution.thirdMax(nums=[2,2,3,1]))


if __name__ == '__main__':
    unittest.main()
