s[:] = s[::-1] 可以，但是s[] = s[::-1]不行，有评论说这样会把逆序赋给原来的s数组，而不会建一个新的对象
虽然python逆序有方法，不过可能不是本题初衷

题解里除了这样解的，还可以用循环镜像来做
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
       
        size = len(s)
		
		# reverse string by mirror image
        for i in range(size//2):
            s[i], s[-i-1] = s[-i-1], s[i]
'''

或者用指针
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:            
        
		# one points to head position, the other points to tail position
        left, right = 0, len(s)-1
        
		# reverse string by two pointers
        while left < right:
            
            s[left], s[right] = s[right], s[left]
            
            left,right = left+1, right-1
'''

或者递归
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:            

        def helper( left:int, right:int, string: List[str]):     
            
            if left >= right:
                # base case
                return
            
            # general case
            s[left], s[right] = s[right], s[left]
            
            helper( left+1, right-1, s)
        # ------------------------------------------------
        
        helper( left = 0, right = len(s)-1, string = s)
'''