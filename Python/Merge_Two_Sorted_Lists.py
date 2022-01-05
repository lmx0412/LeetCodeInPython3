# pylint: disable-all
import unittest
"""
Description:
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

class Solution:
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     node = ListNode(0)
    #     cur = node
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = ListNode(l1.val)
    #             l1 = l1.next
    #             cur = cur.next
    #         else:
    #             cur.next = ListNode(l2.val)
    #             l2 = l2.next
    #             cur = cur.next
    #     if l1:
    #         cur.next = l1
    #     if l2:
    #         cur.next = l2

    #     return node.next

    # def mergeTwoLists(self, l1, l2):
    #     """
    #     # 递归方式
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     node = ListNode(0)
    #     if l1 and l2:
    #         if l1.val > l2.val:
    #             l1, l2 = l2, l1
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1 or l2


class MyTest(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        resultnode = solution.mergeTwoLists(l1, l2)
        result = []
        while resultnode:
            result.append(resultnode.val)
            resultnode = resultnode.next

        self.assertEqual(result, [1, 1, 2, 3, 4, 4])

if __name__ == '__main__':
    unittest.main()
