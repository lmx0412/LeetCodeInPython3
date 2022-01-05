# pylint: disable-all
import unittest
from typing import List
"""
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
 

Constraints:

1 <= timeSeries.length <= 10^4
0 <= timeSeries[i], duration <= 10^7
timeSeries is sorted in non-decreasing order.
"""



class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_damage = 0
        for i, value in enumerate(timeSeries):
            if i == len(timeSeries) - 1:
                total_damage += duration
            else:
                if value + duration < timeSeries[i+1]:
                    total_damage += duration
                else:
                    total_damage += timeSeries[i+1]-timeSeries[i]

        return total_damage

    def findPoisonedDuration_better(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(4, solution.findPoisonedDuration(timeSeries=[1, 4], duration=2))

    def test_example2(self):
        solution = Solution()
        self.assertEqual(3, solution.findPoisonedDuration(timeSeries=[1, 2], duration=2))

    def test_example3(self):
        solution = Solution()
        self.assertEqual(7, solution.findPoisonedDuration(timeSeries=[1, 3, 5], duration=3))


if __name__ == '__main__':
    unittest.main()
