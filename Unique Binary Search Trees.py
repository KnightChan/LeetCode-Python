class Solution:
    # @return an integer
    def numTrees(self, n):
        '''Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
        if n <= 1:
            return 1
        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i // 2):
                f[i] += f[j] * f[i - j - 1] * 2
            if i % 2 == 1:
                f[i] += f[i // 2] * f[i // 2]
        return f[n]

print(10, Solution.numTrees(Solution(), 5))