# pylint: disable-all
import unittest
"""
Description:
    Given a 32-bit signed integer, reverse digits of an integer.

Example1:
    Input: 123
    Output: 321

Example2:
    Input: -123
    Output: -321

Example3:
    Input: 120
    Output: 21

Note:
    Assume we are dealing with an environment which could only store integers within
    the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem,
    assume that your function returns 0 when the reversed integer overflows.
"""

x1 = 123
x2 = -123
x3 = 120
x4 = 1534236469


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == "-":
            x = "-" + x[:0:-1]
        else:
            x = x[::-1]

        if int(x) > 2 ** 31 - 1 or int(x) < -2 ** 31:
            return 0
        return int(x)


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.reverse(x1), 321)
    
    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.reverse(x2), -321)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.reverse(x3), 21)
    
    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.reverse(x4), 0)


if __name__ == '__main__':
    unittest.main()
