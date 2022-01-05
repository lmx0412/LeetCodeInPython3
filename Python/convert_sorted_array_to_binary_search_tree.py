# pylint: disable-all
import unittest

"""
Description:
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p1 = TreeNode(0)
p1.left = TreeNode(-3)
p1.right = TreeNode(9)
p1.left.left = TreeNode(-10)
p1.right.right = TreeNode(5)

p2 = TreeNode(3)
p2.left = TreeNode(1)

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        leftindex = int(len(nums) / 2) - 1
        rightindex = int(len(nums) / 2)
        root = TreeNode(nums[rightindex])
        rightindex += 1
        left, right = root, root
        while leftindex > -1 and rightindex < len(nums):
            left.left = TreeNode(nums[leftindex])
            left = left.left
            right.right = TreeNode(nums[rightindex])
            right = right.right
            leftindex -= 1
            rightindex += 1
        
        if leftindex > -1:
            left.left = TreeNode(nums[leftindex])
        if rightindex < len(nums):
            ritht.right = TreeNode(nums[rightindex])

        return root



class MyTest(unittest.TestCase):
    # def test_example1(self):
    #     solution = Solution()
    #     self.assertEqual(solution.sortedArrayToBST([-10,-3,0,5,9]), p1)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.sortedArrayToBST([1, 3]), p2)


if __name__ == '__main__':
    unittest.main()
