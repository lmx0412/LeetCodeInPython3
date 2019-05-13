# pylint: disable-all
import unittest
"""
Description:
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(2)
p1.left.left = TreeNode(3)
p1.left.right = TreeNode(4)
p1.right.left = TreeNode(4)
p1.right.right = TreeNode(3)



p2 = TreeNode(1)
p2.left = TreeNode(2)
p2.right = TreeNode(2)
p2.left.right = TreeNode(3)
p2.right.right = TreeNode(4)



class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        if left.val == right.val:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        else:
            return False

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.isSymmetric(p1), True)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.isSymmetric(p2), False)



if __name__ == '__main__':
    unittest.main()
