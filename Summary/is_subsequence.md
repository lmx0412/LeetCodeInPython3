最开始用双重循坏来做超时了
第二种思路也不对，看下题解

##### 标记需重刷
题解用了迭代器和生成器，效率非常高，重新学习一下。迭代器会保留上次遍历的位置，如下边测试所示：


```
def iter_test():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = iter(a)

    for i in range(10):
        if 5 in a:
            print(1)
            print(3 in a)

```

输出：
```
1
False
```
可以试试后边所有的list都用迭代器或者生成器来做。（生成器只需要列表推导式改用小括号）