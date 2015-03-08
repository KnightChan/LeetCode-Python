# Filename : Binary Tree Postorder/Preorder Traversal


# Definition for a  binary tree node
# class TreeNode:
# def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        """Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?"""
        return self.doPreNonRecursively_Morris(root)

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        """Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?"""
        return self.doPostNonRecursively_Morris(root)

    def doPostRecursively(self, node):
        if node is None:
            return []
        llist = self.doPostRecursively(node.left)
        rlist = self.doPostRecursively(node.right)
        llist.extend(rlist)
        llist.append(node.val)
        return llist

    def doPostNonRecursively(self, root):
        if root is None:
            return []
        res = []
        stack = []
        status = {}
        stack.append(root)
        status[root] = 0
        while len(stack) > 0:
            node = stack.pop()
            if status[node] == 1:
                res.append(node.val)
                continue
            stack.append(node)
            status[node] = 1
            status[node.right] = 1
            status[node.left] = 1
            if node.right:
                stack.append(node.right)
                status[node.right] = 0
            if node.left:
                stack.append(node.left)
                status[node.left] = 0
        return res

    def doPreRecursively(self, node):
        if node is None:
            return []
        list = [node.val]
        llist = self.doPreRecursively(node.left)
        rlist = self.doPreRecursively(node.right)
        list.extend(llist)
        list.extend(rlist)
        return list

    def doPreNonRecursively(self, root):
        if root is None:
            return []
        res = []
        stack = []
        status = {}
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def doPreNonRecursively_Morris(self, root):
        cur = root
        l = []
        while cur:

            if cur.left:
                rightmost = cur.left
                while rightmost.right and rightmost.right != cur:
                    rightmost = rightmost.right
                if rightmost.right == cur:
                    cur = cur.right
                    rightmost.right = None
                else:
                    l.append(cur.val)
                    rightmost.right = cur
                    cur = cur.left
            else:
                l.append(cur.val)
                cur = cur.right
        return l

    def doPostNonRecursively_Morris(self, root):
        cur = TreeNode(-1)
        cur.left = root
        l = []
        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right and rightmost.right != cur:
                    rightmost = rightmost.right
                if rightmost.right != cur:
                    rightmost.right = cur
                    cur = cur.left
                else:
                    t = cur.left
                    tl = []
                    while t != cur:
                        tl.append(t.val)
                        t = t.right
                    tl.reverse()
                    l += tl
                    rightmost.right = None
                    cur = cur.right
            else:
                cur = cur.right
        return l


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
a.show()
print()
s = Solution()
x = s.postorderTraversal(a)
print(x)