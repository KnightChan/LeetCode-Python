# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        ''' Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.'''
        errlist = []
        self.validBST(root, None, None, errlist)
        if len(errlist) == 0:
            return root
        minn = errlist[0][0]
        maxn = errlist[0][0]
        for item in errlist:
            for x in item:
                if x.val > maxn.val:
                    maxn = x
                if x.val < minn.val:
                    minn = x
        t = minn.val
        minn.val = maxn.val
        maxn.val = t
        return root

    def validBST(self, node, l, r, errlist):
        if node is None:
            return True
        if l and node.val <= l.val:
            errlist.append([l, node])
        if r and node.val >= r.val:
            errlist.append([r, node])
        self.validBST(node.left, l, node, errlist)
        self.validBST(node.right, node, r, errlist)



# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self):
        if self is None:
            return
        print(self.val, end=" ")
        if self.left or self.right:
            if self.left:
                self.left.show()
            else:
                print("#", end=" ")
            if self.right:
                self.right.show()
            else:
                print("#", end=" ")

a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(1)
a.right = b
b.left = c
s = Solution()
x = s.recoverTree(a)
x.show()
print()