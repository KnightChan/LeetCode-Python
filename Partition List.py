# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        '''
        Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5. 
        '''
        def two_list(head, x):
            smallHead = ListNode(0)
            smallTail = smallHead
            largeHead = ListNode(0)
            largeTail = largeHead
            while head:
                if head.val < x:
                    smallTail.next = head
                    smallTail = smallTail.next
                    head = head.next
                    smallTail.next = None
                else:
                    largeTail.next = head
                    largeTail = largeTail.next
                    head = head.next
                    largeTail.next = None
            smallTail.next = largeHead.next
            return smallHead.next
        def two_pointer(head, x):
            dummyHead = ListNode(0)
            dummyHead.next = head
            small = dummyHead
            while small.next and small.next.val < x:
                small = small.next
            nextsmall = small
            while nextsmall.next:
                while nextsmall.next and nextsmall.next.val >= x:
                    nextsmall = nextsmall.next
                if not nextsmall.next:
                    break
                t = nextsmall.next
                nextsmall.next = nextsmall.next.next
                t.next = small.next
                small.next = t
                small = t
            return dummyHead.next
        return two_pointer(head, x)
        #return two_list(head, x)

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


in0 = [1, 4, 3, 5, 2]

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
    print(ss.partition(head.next, 3))
    print()