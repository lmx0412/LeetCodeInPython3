# pylint: disable-all
import unittest
"""
Description:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
    All given inputs are in lowercase letters a-z.
"""

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = []
strs4 = ["aca", "cba"]
strs5 = ["abcd", "ahtrf"]

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(strs1), "fl")

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(strs2), "")

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(strs3), "")

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(strs4), "")

    def test_example5(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(strs5), "a")


if __name__ == '__main__':
    unittest.main()
