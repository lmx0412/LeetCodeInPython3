# pylint: disable-all
import unittest

"""
Description:
    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p1 = TreeNode(3)
p1.left = TreeNode(9)
p1.right = TreeNode(20)
p1.right.left = TreeNode(15)
p1.right.right = TreeNode(7)



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.maxDepth(p1), 3)

    # def test_example2(self):
    #     solution = Solution()
    #     self.assertEqual(solution.maxDepth(p2), False)


if __name__ == '__main__':
    unittest.main()
