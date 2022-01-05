# pylint: disable-all
import unittest
from typing import List
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 10^5
s[i] is a printable ascii character.
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(["o","l","l","e","h"], solution.reverseString(s=["h","e","l","l","o"]))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(["h","a","n","n","a","H"], solution.reverseString(s=["H","a","n","n","a","h"]))

    # def test_example3(self):
    #     solution = Solution()
    #     self.assertEqual(0, solution.countSegments_better(s="                "))

    # def test_example4(self):
    #     solution = Solution()
    #     self.assertEqual(13, solution.countSegments_better(s="Of all the gin joints in all the towns in all the world,   "))

    # def test_example5(self):
    #     solution = Solution()
    #     self.assertEqual(6, solution.countSegments_better(s=", , , ,        a, eaefa"))

    # # def test_example6(self):
    #     solution = Solution()
    #     self.assertEqual([2, 10], solution.countSegments_better(nums=[1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))


if __name__ == '__main__':
    unittest.main()
