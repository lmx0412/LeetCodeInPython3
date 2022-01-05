# pylint: disable-all
import unittest
from typing import List
"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.istitle():
            return True
        if word.isupper():
            return True
        if word.islower():
            return True

        return False

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(True, solution.detectCapitalUse(word="USA"))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(False, solution.detectCapitalUse(word="FlAG"))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(True, solution.detectCapitalUse(word="Flaag"))

    # def test_example4(self):
    #     solution = Solution()
    #     self.assertEqual([2, 1], solution.detectCapitalUse(nums=[2, 2]))

    # def test_example5(self):
    #     solution = Solution()
    #     self.assertEqual([2, 1], solution.detectCapitalUse(nums=[2, 3, 2]))

    # def test_example6(self):
    #     solution = Solution()
    #     self.assertEqual([2, 10], solution.detectCapitalUse(nums=[1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))


if __name__ == '__main__':
    unittest.main()
