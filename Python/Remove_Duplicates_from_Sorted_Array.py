# pylint: disable-all
import unittest

"""
Description:
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example1:
    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.

Example2:
    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.

Clarification:

    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

    Internally you can think of this:

        // nums is passed in by reference. (i.e., without making a copy)
        int len = removeDuplicates(nums);

        // any modification to nums in your function would be known by the caller.
        // using the length returned by your function, it prints the first len elements.
        for (int i = 0; i < len; i++) {
            print(nums[i]);
        }
"""
num1 = [1, 1, 2]
num2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

class Solution:
    def removeDuplicates(self, nums):
        cur = 1
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        while cur < len(nums):
            if nums[cur] == nums[cur - 1]:
                nums.pop(cur)
            else:
                cur += 1

        return len(nums)

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates(num1), [1, 2])
        self.assertEqual(len(solution.removeDuplicates(num1)), 2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates(num2), [0, 1, 2, 3, 4])
        self.assertEqual(len(solution.removeDuplicates(num2)), 5)

    # def test_example3(self):
    #     solution = Solution()
    #     self.assertEqual(solution.mergeTwoLists(s3), False)

    # def test_example4(self):
    #     solution = Solution()
    #     self.assertEqual(solution.mergeTwoLists(s4), False)

    # def test_example5(self):
    #     solution = Solution()
    #     self.assertEqual(solution.mergeTwoLists(s5), True)

    # def test_example6(self):
    #     solution = Solution()
    #     self.assertEqual(solution.mergeTwoLists(s6), False)


if __name__ == '__main__':
    unittest.main()
