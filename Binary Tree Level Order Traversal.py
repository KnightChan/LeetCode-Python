# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        '''Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.'''
        if root is None:
            return []
        queue = [[root, 0]]
        res = []
        curdepth = 0
        curlist = []
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth > curdepth:
                curdepth = depth
                res.append(list(curlist))
                curlist = []
            curlist.append(node.val)
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        res.append(list(curlist))
        return res