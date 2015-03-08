# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#the online judge has already import headq, so del the next line to submit
import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        '''
        Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
        '''
        dic = {}
        
        heap = []
        heapq.heapify(heap)
        for l in lists:
            if l:
                if l.val not in dic:
                    dic[l.val] = []
                    heapq.heappush(heap, l.val)
                dic[l.val].append(l)
        dummyHead = ListNode(0)
        tdh = dummyHead
        while True:
            if len(heap) == 0:
                break
            x = heapq.heappop(heap)
            for l in dic[x]:
                t = l
                l = l.next
                if l:
                    if l.val not in dic:
                        dic[l.val] = []
                        heapq.heappush(heap, l.val)
                    dic[l.val].append(l)
                t.next = None
                tdh.next = t
                tdh = t
            del dic[x]
        return dummyHead.next
