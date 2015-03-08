# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    '''Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.'''
    def inorderTraversal(self, root):
        return self.inorderTraversal_Morris(root)

    def __init__(self):
        self.l = []

    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal_Recursive(self, root):
        if root is None:
            return []
        self.inorderTraversal(root.left)
        self.l.append(root.val)
        self.inorderTraversal(root.right)
        return self.l

    def inorderTraversal_Stack(self, root):
        if root is None:
            return []
        stack = [[root, 0]]
        l = []
        while len(stack) > 0:
            node, state = stack.pop()
            if state == 1:
                l.append(node.val)
                continue
            if node.right:
                stack.append([node.right, 0])
            stack.append([node, 1])
            if node.left:
                stack.append([node.left, 0])
        return l

    def inorderTraversal_Morris(self, root):
        if root is None:
            return []
        l = []
        cur = root
        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right and rightmost.right != cur:
                    rightmost = rightmost.right
                if not rightmost.right:
                    rightmost.right = cur
                    cur = cur.left
                else:
                    l.append(cur.val)
                    cur = cur.right
                    rightmost.right = None
            else:
                l.append(cur.val)
                cur = cur.right
        return l
