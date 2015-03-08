# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        '''
        Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
        '''
        if not head:
            return None
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        n = n - k % n
        tail.next = head
        t = head
        while n > 1:
            t = t.next
            n -= 1
        head = t.next
        t.next = None
        return head
