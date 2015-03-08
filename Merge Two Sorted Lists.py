# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        '''
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
        '''
        dummyHead = ListNode(0)
        th = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                th.next = l1
                l1 = l1.next
            else:
                th.next = l2
                l2 = l2.next
            th = th.next
        if l1:
            th.next = l1
        if l2:
            th.next = l2
        return dummyHead.next
