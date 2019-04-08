# pylint: disable-all
import unittest

"""
Description:
    Implement int sqrt(int x).

    Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

    Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
    Input: 4
    Output: 2

Example 2:
    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                the decimal part is truncated, 2 is returned.

"""
x1 = 4
x2 = 8
x3 = 1


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        
        while left <= right:
            mid = left + (right - left)//2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return mid

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(x1), 2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(x2), 2)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.mySqrt(x3), 1)



if __name__ == '__main__':
    unittest.main()
