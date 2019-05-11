# pylint: disable-all
import unittest
"""
Description:
    Given two binary trees, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)


p2 = TreeNode(1)
p2.left = TreeNode(2)
q2 = TreeNode(1)
q2.right = TreeNode(2)

p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)
q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree(p1, q1), True)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree(p2, q2), False)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree(p3, q3), False)




if __name__ == '__main__':
    unittest.main()
