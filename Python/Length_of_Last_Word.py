# pylint: disable-all
import unittest

"""
Description:
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""
s1 = "Hello World"
s2 = "a "
s3 = ""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return(len(s.rstrip().split(' ')[-1]))


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s1), 5)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s2), 1)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s3), 0)





if __name__ == '__main__':
    unittest.main()
