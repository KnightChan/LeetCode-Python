#coding:utf-8
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        '''
         Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. 
        '''
        dummyHead = ListNode(0)
        dummyHead.next = head
        postPre = None
        preTail = None
        revHead = None
        t = dummyHead
        k = 0
        while k < n:
            if k == m - 1:
                preTail = t
                revHead = t.next
            k += 1
            t = t.next
        postPre = t.next
        t.next = None
        def reverseList(head):
            pre = None
            tail = head
            while head:
                t = head
                head = head.next
                t.next = pre
                pre = t
            return [pre, tail]
        revHead, revTail = reverseList(revHead)
        preTail.next = revHead
        revTail.next = postPre
        return dummyHead.next

