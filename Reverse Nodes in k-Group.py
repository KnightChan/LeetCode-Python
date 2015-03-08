# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        '''
         Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 
        '''
        fast = head
        slow = head
        dummyHead = ListNode(0)
        dummyHead.next = head
        dht = dummyHead
        while fast:
            for i in range(k):
                if not fast:
                    dht.next = slow
                    return dummyHead.next
                fast = fast.next
            thisk = self.reverseList(slow, fast)
            dht.next = thisk[0]
            dht = thisk[1]
            slow = fast
        return dummyHead.next

    def reverseList(self, start, end):
        pre = None
        t = start
        while t != end:
            x = t.next
            t.next = pre
            pre = t
            t = x
        return [pre, start]

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
in1 = [1, 2, 3]
in2 = [1]

ins = [in1]

for tin in ins:
    head = ListNode(0)
    tail = head
    for val in tin:
        tail.next = ListNode(val)
        tail = tail.next
    ss = Solution()
    print(len(tin), tin)
    # print(head)
    print(ss.reverseKGroup(head.next, 2))
    print()