# pylint: disable-all
import unittest
from typing import List
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return self.__is_palindrome(s)

    def __is_palindrome(self, s):
        if not s: return True
        while len(s) >= 2:
            if s.pop(0) == s.pop(-1):
                continue
            else:
                return False

        return True

    def isPalindrome_better(self, s):
        newS = [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]
        #return newS[:len(newS)/2] == newS[(len(newS)+1)/2:][::-1]  # This one is better, but too long

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(True, solution.isPalindrome(s="A man, a plan, a canal: Panama"))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(False, solution.isPalindrome(s="race a car"))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(True, solution.isPalindrome(s=" "))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(False, solution.isPalindrome(s="0P"))

    # def test_example5(self):
    #     solution = Solution()
    #     self.assertEqual([2, 1], solution.isPalindrome(nums=[2, 3, 2]))

    # def test_example6(self):
    #     solution = Solution()
    #     self.assertEqual([2, 10], solution.isPalindrome(nums=[1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))


if __name__ == '__main__':
    unittest.main()
