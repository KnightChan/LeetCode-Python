# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        '''Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. '''
        if len(inorder) == 0:
            return None
        rootval = postorder.pop()
        leftNum = inorder.index(rootval)
        rightNum = len(inorder) - 1 - leftNum
        node = TreeNode(rootval)
        node.left = self.buildTree(inorder[0:leftNum], postorder[0:leftNum])
        node.right = self.buildTree(inorder[leftNum + 1:], postorder[leftNum:leftNum + rightNum])
        return node

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None