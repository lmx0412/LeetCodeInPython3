
####思路:
用python内置函数很简单,找元素,找到了返回index,没找到append入list,排序,返回index
用遍历的方法注意边界条件,但是运行时间反而不如python内置方法...(又试了一次,好像runtime不稳定,不用太介意这个了)

有个答案很好:
'''
return len([x for x in nums if x<target])
'''
不过貌似效率不高,可能列表推导有额外的消耗

标准思路好像是用二分法,同样需要注意边界条件
