# pylint: disable-all
import unittest
from typing import List
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        i, j = 0, 0
        while i != len(s):
            while j != len(t):
                if s[i] == t[j] and i == len(s) - 1:
                    return True
                elif s[i] == t[j] and i != len(s) - 1:
                    i += 1
                    j += 1
                    break
                elif s[i] != t[j] and j == len(s) - 1:
                    return False
                else:
                    j += 1
            
        return False

    def isSubsequence_better(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        s, t = list(s), list(t)
        sequence = []
        for i in range(len(s)):
            if s[i] in t:
                sequence.append(t.index(s[i]))
                t.remove(s[i])
            else:
                return False
        
        return sequence == sorted(sequence)

    def isSubsequence_iter(self, s: str, t: str) -> bool:
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(True, solution.isSubsequence_iter(s="abc", t="ahbgdc"))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(False, solution.isSubsequence_iter(s="axc", t="ahbgdc"))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(False, solution.isSubsequence_iter(s="acb", t="ahbgdc"))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(True, solution.isSubsequence_iter(s="ab", t="baab"))


if __name__ == '__main__':
    unittest.main()
