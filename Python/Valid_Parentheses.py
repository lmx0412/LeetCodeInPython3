# pylint: disable-all
import unittest
"""
Description:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true

Example 2:
    Input: "()[]{}"
    Output: true

Example 3:
    Input: "(]"
    Output: false

Example 4:
    Input: "([)]"
    Output: false

Example 5:
    Input: "{[]}"
    Output: true
"""
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
s6 = "){"

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        if len(s) == 0:
            return True
        DICT = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for item in s:
            if item in DICT:
                stack.append(DICT[item])
            else:
                if not stack or stack.pop() != item:
                    return False
        if stack:
            return False
        return True


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s1), True)

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s2), True)

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s3), False)

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s4), False)

    def test_example5(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s5), True)
    
    def test_example6(self):
        solution = Solution()
        self.assertEqual(solution.isValid(s6), False)


if __name__ == '__main__':
    unittest.main()
