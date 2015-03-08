# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        ''' Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.'''
        return self.validBST(root, 0, 0, False, False)

    def validBST(self, node, l, r, lv, rv):
        if node is None:
            return True
        if lv and node.val <= l:
            return False
        if rv and node.val >= r:
            return False
        lchild = self.validBST(node.left, l, node.val, lv, True)
        rchild = self.validBST(node.right, node.val, r, True, rv)
        return lchild and rchild