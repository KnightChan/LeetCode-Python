# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        """ Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}. """
        size = 0
        lhead = head
        rhead = head
        while rhead:
            size += 1
            rhead = rhead.next
        if size <= 1:
            return head
        halfsize = size - size // 2
        rhead = head
        tmp = None
        while halfsize > 0:
            if halfsize == 1:
                tmp = rhead
            rhead = rhead.next
            halfsize -= 1
        tmp.next = None
        #print('rhead : ', rhead)

        rhead = self.reverseList(rhead)

        #print('lhead : ', lhead)
        #print('rhead : ', rhead)

        head = lhead
        while rhead:
            lnext = lhead.next
            tmp = rhead
            rhead = rhead.next
            lhead.next = tmp
            tmp.next = lnext
            lhead = lnext

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        pnext = head.next
        head.next = None
        while pnext:
            tmp = pnext
            pnext = pnext.next
            tmp.next = head
            head = tmp
        return head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        # print("in str")
        tmp = self
        strs = []
        while tmp.next is not None:
            strs.append(str(tmp.val) + "->")
            tmp = tmp.next
        else:
            strs.append(str(tmp.val) + ";")
        return "".join(strs)

in0 = [1, 2, 3, 4]

ins = [in0]

for tin in ins:
    head = ListNode(0)
    tail = head
    for val in tin:
        tail.next = ListNode(val)
        tail = tail.next
    ss = Solution()
    print(len(tin), tin)
    print(head)
    ss.reorderList(head.next)
    print(head.next)
    print()