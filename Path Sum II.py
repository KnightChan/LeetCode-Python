# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        ''' Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''
        reslist = []
        self.dfs(root, 0, [], sum, reslist)
        return reslist

    def dfs(self, node, cursum, curlist, sum, reslist):
        if node is None:
            return
        if node.left is None and node.right is None:
            if cursum + node.val == sum:
                curlist.append(node.val)
                reslist.append(list(curlist))
                curlist.pop()
            return
        curlist.append(node.val)
        self.dfs(node.left, cursum + node.val, curlist, sum, reslist)
        curlist.pop()
        curlist.append(node.val)
        self.dfs(node.right, cursum + node.val, curlist, sum, reslist)
        curlist.pop()
