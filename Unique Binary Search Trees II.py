# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        '''
        Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
        '''
        def genTree(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r + 1):
                left = genTree(l, i - 1)
                right = genTree(i + 1, r)
                for j in range(len(left)):
                    for k in range(len(right)):
                        node = TreeNode(i)
                        node.left = left[j]
                        node.right = right[k]
                        res.append(node)
            return res
        return genTree(1, n)
