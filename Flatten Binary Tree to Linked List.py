# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        ''' Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return node
        if not node.left and not node.right:
            return node
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        if l is None:
            return r
        elif r is None:
            node.right = node.left
            node.left = None
            return l
        else:
            l.right = node.right
            node.right = node.left
            node.left = None
            return r
