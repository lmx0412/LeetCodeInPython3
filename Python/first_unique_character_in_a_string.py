# pylint: disable-all
import unittest
from typing import List
"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        s = list(s)
        for i, c in enumerate(s):
            if c in seen.keys():
                seen[c] = float("Inf")
            else:
                seen[c] = i

        return min(seen.values()) if min(seen.values()) != float("Inf") else -1


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(0, solution.firstUniqChar(s="leetcode"))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(2, solution.firstUniqChar(s="loveleetcode"))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(-1, solution.firstUniqChar(s="aabb"))

    def test_example4(self):
        solution = Solution()
        self.assertEqual(-1, solution.firstUniqChar(s="aadadaad"))

if __name__ == '__main__':
    unittest.main()
