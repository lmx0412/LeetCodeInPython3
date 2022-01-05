# pylint: disable-all
import unittest
"""

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""



class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        string = "".join([str(i) for i in nums])
        split_string = string.split("0")
        for i, value in enumerate(split_string):
            split_string[i] = len(value)
        
        return max(split_string)

    def findMaxConsecutiveOnes_better(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

    def findMaxConsecutiveOnes_oneline(self, nums) -> int:
        return max(list(map(len, ("".join(list(map(str, nums)))).split('0'))))

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(3, solution.findMaxConsecutiveOnes_better(nums=[1, 1, 0, 1, 1, 1]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(2, solution.findMaxConsecutiveOnes_better(nums=[1, 0, 1, 1, 0, 1]))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(4, solution.findMaxConsecutiveOnes_better(nums=[1, 0, 1, 1, 1, 1, 0, 1]))


if __name__ == '__main__':
    unittest.main()
