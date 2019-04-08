# pylint: disable-all
import unittest

"""
Description:
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.

Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step.

"""
n1 = 2
n2 = 3
n3 = 4
n4 = 1


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        res = [1, 2]
        while len(res) < n:
            res.append(res[-1] + res[-2])
        
        return res[-1]


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(n1), 2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(n2), 3)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(n3), 5)

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(n4), 1)



if __name__ == '__main__':
    unittest.main()
