# pylint: disable-all
import unittest

"""
Description:
    Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

"""
a1 = "11"
b1 = "1"
a2 = "1010"
b2 = "1011"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(eval("0b" + a) + eval("0b" + b))).replace("0b", "")


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.addBinary(a1, b1), "100")

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.addBinary(a2, b2), "10101")


if __name__ == '__main__':
    unittest.main()
