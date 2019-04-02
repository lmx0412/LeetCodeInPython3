# pylint: disable-all
import unittest

"""
Description:
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""
nums1 = [1, 3, 5, 6]
target1 = 5
nums2 = [1, 3, 5, 6]
target2 = 2
nums3 = [1, 3, 5, 6]
target3 = 7
nums4 = [1, 3, 5, 6]
target4 = 0
nums5 = [1, 3]
target5 = 2



class Solution:
    def searchInsert(self, nums, target):
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)
        
        for index in range(len(nums)):
            if nums[index] == target:
                return index
            if nums[index] > target:
                return index
        return len(nums)

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert(nums1, target1), 2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert(nums2, target2), 1)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert(nums3, target3), 4)

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert(nums4, target4), 0)


    def test_example5(self):
        solution = Solution()
        self.assertEqual(solution.searchInsert(nums5, target5), 1)



if __name__ == '__main__':
    unittest.main()
