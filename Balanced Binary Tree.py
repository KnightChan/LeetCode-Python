# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        '''Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. '''
        return self.dfs(root)[0]

    def dfs(self, node):
        if node is None:
            return [0, True]
        l, lb = self.dfs(node.left)
        r, rb = self.dfs(node.right)
        max_height = max(l, r) + 1
        if abs(l - r) > 1:
            return [max_height, False]
        else:
            return [max_height, True and lb and rb]
