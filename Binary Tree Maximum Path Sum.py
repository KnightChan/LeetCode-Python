# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        ''' Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6. '''
        sumwithroot, maxSum = self.maxTreeSum(root)
        return maxSum
    
    def maxTreeSum(self, node):
        if node is None:
            return [0, 0]
        sum = node.val
        tmax = node.val
        l, lmax = self.maxTreeSum(node.left)
        r, rmax = self.maxTreeSum(node.right)
        if node.left is not None:
            sum = max(sum, l + node.val)
            tmax = max(tmax, sum, l, lmax)
        if node.right is not None:
            sum = max(sum, r + node.val)
            tmax = max(tmax, sum, r, rmax)
        if node.left and node.right:
            tmax = max(tmax, l + r + node.val)
        return [sum, tmax]
