# pylint: disable-all
import unittest

"""
Description:
    Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
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
    def levelOrderBottom(self, root: TreeNode):
        self.ret = []
        self.find_next(0, root)

        return self.ret


    def find_next(self, level, root):
        if root:
            if len(self.ret) < level + 1:
                self.ret.insert(0, [])
            self.ret[-(level+1)].insert(0, root.val)
            self.find_next(level + 1, root.right)
            self.find_next(level + 1, root.left)
            


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.levelOrderBottom(p1), [[15, 7], [9, 20], [3]])

    # def test_example2(self):
    #     solution = Solution()
    #     self.assertEqual(solution.maxDepth(p2), False)


if __name__ == '__main__':
    unittest.main()
