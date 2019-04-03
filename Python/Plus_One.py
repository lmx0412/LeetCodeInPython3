# pylint: disable-all
import unittest

"""
Description:
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:
    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

"""
digits1 = [1, 2, 3]
digits2 = [4, 3, 2, 1]
digits3 = []
digits4 = [9]


class Solution:
    def plusOne(self, digits):
        if not digits:
            return [1]

        s1, ret = "", []
        for num in digits:
            s1 += str(num)

        s1 = str(int(s1) + 1)
        for i in range(len(s1)):
            ret.append(int(s1[i]))

        return ret

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.plusOne(digits1), [1, 2, 4])

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.plusOne(digits2), [4, 3, 2, 2])

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.plusOne(digits3), [1])

    def test_example4(self):
        solution = Solution()
        self.assertEqual(solution.plusOne(digits4), [1, 0])



if __name__ == '__main__':
    unittest.main()


