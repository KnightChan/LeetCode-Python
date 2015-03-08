class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        ''' Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false. '''
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        f = [[False] * (l2 + 1) for row in range(l1 + 1)]
        f[0][0] = True
        for i in range(1, l1 + 1):
            if s1[:i] == s3[:i]:
                f[i][0] = True
        for i in range(1, l2 + 1):
            if s2[:i] == s3[:i]:
                f[0][i] = True
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                f[i][j] = (f[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                          (f[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return f[l1][l2]

s0 = ["aabcc", "dbbca", "aadbbcbcac"]
s1 = ["aabcc", "dbbca", "aadbbbaccc"]
a = s1
s = Solution()
print(s.isInterleave(a[0], a[1], a[2]))