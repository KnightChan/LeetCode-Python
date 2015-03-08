# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        '''
         Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 
        '''
        dummyHead = ListNode(0)
        dummyHead.next = head
        t = dummyHead
        while t:
            n1 = t.next
            if not t.next:
                return dummyHead.next
            n2 = t.next.next
            if not t.next.next:
                return dummyHead.next
            next = t.next.next.next
            n2.next = n1
            n1.next = next
            t.next = n2
            t = n1
        return dummyHead.next
        