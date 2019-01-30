# pylint: disable-all
import unittest
"""
Description:
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example1:
    Input: 121
    Output: true

Example2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
    Coud you solve it without converting the integer to a string?
"""

x1 = 121
x2 = -121
x3 = 10
x4 = 1
x5 = 0
x6 = 11

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 1:
            return True
        elif len(x) % 2 == 1:
            return x[int(len(x)/2):][::-1] == x[:int(len(x)/2) + 1]
        else:
            return x[int(len(x)/2):][::-1] == x[:int(len(x)/2)]




class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x1), True)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x2), False)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x3), False)
    
    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x4), True)
    
    def test_example5(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x5), True)

    def test_example6(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome(x6), True)


if __name__ == '__main__':
    unittest.main()

