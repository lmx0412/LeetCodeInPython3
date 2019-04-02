# pylint: disable-all
import unittest

"""
Description:
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.

    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
haystack3 = "hello"
needle3 = "lo"


class Solution:
    def strStr(self, haystack, needle):
        # return haystack.find(needle)
        if needle is None or needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.strStr(haystack1, needle1), 2)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.strStr(haystack2, needle2), -1)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.strStr(haystack3, needle3), 3)


if __name__ == '__main__':
    unittest.main()
