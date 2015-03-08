# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        """Sort a linked list in O(n log n) time using constant space complexity."""
        #print(head)
        return self.mergeList(head)

    def mergeList(self, node):
        #print('merge start', node)
        snode = node
        size = 0
        lh = None
        rh = None
        while node is not None:
            size += 1
            tmp = node
            node = node.next
            if size % 2:
                tmp.next = lh
                lh = tmp
            else:
                tmp.next = rh
                rh = tmp
        #print('size = ', size)
        #print("return: " + str(snode))
        if size <= 1:
            return snode
        #print("lh : " + str(lh))
        #print("rh : " + str(rh))

        lres = self.mergeList(lh)
        rres = self.mergeList(rh)
        #print("lres : " + str(lres))
        #print("rres : " + str(rres))
        res = self.mergeSortedList(lres, rres)
        #print('merge end', res)
        return res

    def mergeSortedList(self, lh, rh):
        tlh = lh
        #print('sorted list start')
        while rh is not None:
            if lh.val > rh.val:
                tmpnode = rh
                rh = rh.next
                tmpnode.next = lh
                lh = tmpnode
                tlh = lh
                continue
            while lh.next is not None and lh.next.val < rh.val:
                lh = lh.next
            if lh.next is None and lh.val < rh.val:
                lh.next = rh
                break
            tmpnode = rh
            rh = rh.next
            tmpnode.next = lh.next
            lh.next = tmpnode
        #print('sorted list end')
        return tlh

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        #print("in str")
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
    #print(head)
    print(ss.sortList(head.next))
    print()