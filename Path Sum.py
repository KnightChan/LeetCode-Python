# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        ''' Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.'''
        return self.dfs(root, 0, sum)

    def dfs(self, node, cursum, sum):
        if node is None:
            return False
        if node.left is None and node.right is None:
            return cursum + node.val == sum
        return self.dfs(node.left, cursum + node.val, sum) or self.dfs(node.right, cursum + node.val, sum)
