# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        ''' A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list. '''
        if head is None:
            return None
        tp = head
        while tp is not None:
            tpc = RandomListNode(tp.label)
            tpc.next = tp.next
            tp.next = tpc
            tp = tpc.next
        tp = head
        while tp is not None:
            if tp.random is not None:
                tp.next.random = tp.random.next
            tp = tp.next.next
        h1 = head
        h2 = head.next
        tp = head
        while tp.next is not None:
            t = tp.next
            tp.next = tp.next.next
            tp = t
        head = h1
        return h2

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def __str__(self):
        #print("in str")
        tmp = self
        if tmp is None:
            return "None!"
        strs = []
        while tmp.next is not None:
            x = "N"
            if tmp.random is not None:
                x = str(tmp.random.label)
            strs.append("(" + str(tmp.label) + "," + x + ")->")
            tmp = tmp.next
        else:
            x = "N"
            if tmp.random is not None:
                x = str(tmp.random.label)
            strs.append("(" + str(tmp.label) + "," + x + ");")
        return "".join(strs)

in0 = [1, 2, 2, 2]

ins = [in0]

for tin in ins:
    head = RandomListNode(0)
    tail = head
    for val in tin:
        tail.next = RandomListNode(val)
        tail = tail.next
    ss = Solution()
    print(len(tin), tin)
    print(head.next)
    print(ss.copyRandomList(head.next))
    print(head.next)
    print()