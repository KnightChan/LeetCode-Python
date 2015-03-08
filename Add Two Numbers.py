# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        '''
        You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
        '''
        t1 = l1
        t2 = l2
        ex = 0
        l3 = ListNode(0)
        t3 = l3
        while t1 or t2:
            if t1 is None:
                n1 = 0
            else:
                n1 = t1.val
                t1 = t1.next
            if t2 is None:
                n2 = 0
            else:
                n2 = t2.val
                t2 = t2.next
            t3.next = ListNode((n1 + n2 + ex) % 10)
            ex = (n1 + n2 + ex) // 10
            t3 = t3.next
        if ex == 1:
            t3.next = ListNode(1)
            t3 = t3.next
        return l3.next
            