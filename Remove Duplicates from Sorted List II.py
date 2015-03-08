# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        '''
         Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
        '''
        dummyHead = ListNode(-1)
        dummyHead.next = head
        t = dummyHead
        while t:
            while t.next and t.next.next and t.next.val == t.next.next.val:
                del_v = t.next.val
                while t.next and t.next.val == del_v:
                    t.next = t.next.next
            t = t.next
        return dummyHead.next
