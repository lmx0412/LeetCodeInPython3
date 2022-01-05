# pylint: disable-all
import unittest
from typing import List
"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.



Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
 

Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
"""


class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        s = s.split(" ")
        s = [i for i in s if i.strip()]
        return len(s)

    def countSegments_better(self, s: str) -> int:
        return len(s.split())

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(5, solution.countSegments_better(s="Hello, my name is John"))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(1, solution.countSegments_better(s="Hello"))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(0, solution.countSegments_better(s="                "))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(13, solution.countSegments_better(s="Of all the gin joints in all the towns in all the world,   "))

    def test_example5(self):
        solution = Solution()
        self.assertEqual(6, solution.countSegments_better(s=", , , ,        a, eaefa"))

    # def test_example6(self):
    #     solution = Solution()
    #     self.assertEqual([2, 10], solution.countSegments_better(nums=[1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))


if __name__ == '__main__':
    unittest.main()
