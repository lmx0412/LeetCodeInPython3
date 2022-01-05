第一次用List.count()方法直接超时，这么做时间复杂度应该是O(n^2)
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s  = list(s)
        for item in s:
            if s.count(item) == 1:
                return s.index(item)
        return -1
'''
用find方法应该可以，但是还是试试不用

换了个dict记录的方式，时间效率还是比较低
题解也没有特别亮眼的
