原解法能过

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return ""
        minlen = len(strs[0])
        for item in strs:
            if len(item) < minlen:
                minlen = len(item)
        
        for i in range(minlen):
            tmp = strs[0][i]
            for item in strs:
                if item[i] != tmp:
                    tmp = ""
                    res += tmp
                    return res
            res += tmp
        return res

本题可以使用zip和set

如果各个迭代器的元素个数不一致，则zip返回列表长度与最短的对象相同
如 strs1 = ["flower", "flow", "flight"]
list(zip(*str1))为[('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
注意此处不加*组包的话list(zip(str1))为[('flower',), ('flow',), ('flight',)]

后续判断比较简单，使用set去重，超过1 break即可
