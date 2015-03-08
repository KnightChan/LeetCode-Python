# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        '''Given an array where elements are sorted in ascending order, convert it to a height balanced BST.'''
        return self.dfs(0, len(num) - 1, num)

    def dfs(self, l, r, num):
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(num[mid])
        node.left = self.dfs(l, mid - 1, num)
        node.right = self.dfs(mid + 1, r, num)
        return node

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

s = Solution()
r = s.sortedArrayToBST([1,2,3,4])
print(r)