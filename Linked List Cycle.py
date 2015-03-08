# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        """ Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space? """
        if head is None:
            return False
        slow = head
        fast = head.next
        m = 1
        while slow and fast and slow != fast:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            m += 1
        if slow is None or fast is None:
            return False
        return True


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


in0 = [1, 2, 4, 3, 2]

ins = [in0]

for tin in ins:
    head = ListNode(0)
    tail = head
    for val in tin:
        tail.next = ListNode(val)
        tail = tail.next
    ss = Solution()
    print(len(tin), tin)
    # print(head)
    print(ss.hasCycle(head.next))
    print()