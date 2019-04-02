
####思路:
找子串,注意边界条件即可
用find也行不过有点投机取巧
看到一个答案,里边的index用法值得注意:

'''
if(needle not in haystack):
    return(-1)
return(haystack.index(needle))
'''
