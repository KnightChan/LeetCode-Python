# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        '''Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. '''
        if len(inorder) == 0:
            return None
        rootval = preorder.pop(0)
        leftNum = inorder.index(rootval)
        rightNum = len(inorder) - 1 - leftNum
        node = TreeNode(rootval)
        node.left = self.buildTree(preorder[0:leftNum], inorder[0:leftNum])
        node.right = self.buildTree(preorder[leftNum:leftNum + rightNum], inorder[leftNum + 1:])
        return node

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

s = Solution()
s.buildTree([1,4,2,3], [1,2,3,4])