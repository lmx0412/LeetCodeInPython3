# pylint: disable-all
import unittest
"""
Description:
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
    Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]
"""

nums11 = [1, 2, 3, 0, 0, 0]
nums21 = [2, 5, 6]
m1 = 3
n1 = 3

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2, end = m - 1, n - 1, m + n - 1
        while index1 >= 0 and index2 >=0:
            if nums1[index1] >= nums2[index2]:
                nums1[end] = nums1[index1]
                index1 -= 1
            else:
                nums1[end] = nums2[index2]
                index2 -= 1
            end -= 1

        if index2 >= 0:
            nums1[: index2 + 1] = nums2[: index2 + 1]

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        solution.merge(nums11, n1, nums21, m1)
        self.assertEqual(nums11, [1, 2, 2, 3, 5, 6])

    


if __name__ == '__main__':
    unittest.main()
