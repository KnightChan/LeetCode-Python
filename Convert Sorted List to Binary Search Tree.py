# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        '''Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.'''
        n = 0
        t = head
        while t:
            n += 1
            t = t.next
        return self.dfs([head], 0, n - 1)

    def dfs(self, t, l, r):
        if r < l:
            return None
        mid = (l + r) // 2
        lchild = self.dfs(t, l, mid - 1)
        parent = TreeNode(t[0].val)
        t[0] = t[0].next
        #print(l, r, mid, parent.val)
        parent.left = lchild
        parent.right = self.dfs(t, mid + 1, r)
        return parent

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(3)
b = ListNode(5)
c = ListNode(8)
d = ListNode(10)
e = ListNode(13)
a.next = b
b.next = c
c.next = d
d.next = e
s = Solution()
r = s.sortedListToBST(a)
