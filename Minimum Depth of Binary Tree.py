# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        '''Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.'''
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        queue = [[root, 1]]
        while len(queue):
            node, depth = queue.pop(0)
            if node.left:
                if node.left.left is None and node.left.right is None:
                    return depth + 1
                queue.append([node.left, depth + 1])
            if node.right:
                if node.right.left is None and node.right.right is None:
                    return depth + 1
                queue.append([node.right, depth + 1])
