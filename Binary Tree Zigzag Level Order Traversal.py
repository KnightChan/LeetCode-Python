# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        '''Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.'''
        if root is None:
            return []
        queue = [[root, 0]]
        res = []
        curdepth = 0
        curlist = []
        reverse = False
        while len(queue) > 0:
            node, depth = queue.pop(0)
            if depth > curdepth:
                curdepth = depth
                if reverse:
                    curlist.reverse()
                reverse = not reverse
                res.append(list(curlist))
                curlist = []
            curlist.append(node.val)
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        if reverse:
            curlist.reverse()
        res.append(list(curlist))
        return res