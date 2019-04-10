# pylint: disable-all
import unittest

"""
Description:
    Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
    Input: 1->1->2
    Output: 1->2

Example 2:
    Input: 1->1->2->3->3
    Output: 1->2->3

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(3)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ret = ListNode(None)
        tmp = ret
        while head:
            if head.val != tmp.val:
                tmp.next = ListNode(head.val)
                head = head.next
                tmp = tmp.next
            else:
                head = head.next
        
        return ret.next

class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        result = []
        resultnode = solution.deleteDuplicates(l1)
        while resultnode:
            result.append(resultnode.val)
            resultnode = resultnode.next

        self.assertEqual(result, [1, 2])

    def test_example2(self):
        solution = Solution()
        result = []
        resultnode = solution.deleteDuplicates(l2)
        while resultnode:
            result.append(resultnode.val)
            resultnode = resultnode.next
        
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
