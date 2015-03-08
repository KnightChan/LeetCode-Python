# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        """ Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space? """
        if head is None:
            return head
        slow = head
        fast = head.next
        while slow and fast and slow != fast:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
        if slow is None or fast is None:
            return None
        tmp = slow.next
        cyclesize = 1
        while tmp != slow:
            tmp = tmp.next
            cyclesize += 1
        #print(x, m, cyclesize, slow.val)
        x = cyclesize
        p2 = head
        p1 = head
        while x > 0:
            p2 = p2.next
            x -= 1
        while p2 != p1:
            p2 = p2.next
            p1 = p1.next
        return p2

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


in0 = [3, 2, 0, -4]

ins = [in0]

for tin in ins:
    head = ListNode(0)
    tail = head
    for val in tin:
        tail.next = ListNode(val)
        tail = tail.next
    ss = Solution()
    print(head)
    tail.next = head.next.next
    print(ss.detectCycle(head.next).val)
    print()