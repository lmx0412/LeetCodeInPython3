# pylint: disable-all
import unittest

"""
Description:
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:
    Input: 1
    Output: "1"

Example 2:
    Input: 4
    Output: "1211"
"""
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6

class Solution:
    def countAndSay(self, n: int) -> str:
        ret = "1"
        for _ in range(n - 1):
            tmp, count, res = ret[0], 0, ""
            for s in ret:
                if s == tmp:
                    count += 1
                else:
                    res += str(count) + tmp
                    count = 1
                    tmp = s
            res += str(count) + tmp
            ret = res

        return ret


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n1), "1")

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n2), "11")

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n3), "21")

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n4), "1211")

    def test_example5(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n5), "111221")

    def test_example6(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(n6), "312211")



if __name__ == '__main__':
    unittest.main()
