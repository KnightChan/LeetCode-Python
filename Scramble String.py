class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        '''
         Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1. 
        '''
        n = len(s1)
        if n != len(s2):
            return False
        if n == 0:
            return True
        dp = [[[False] * n for col in range(n)] for row in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = (s1[i] == s2[j])
                dp[0][i][j] = True
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if (dp[k][i][j] and dp[l-k][i+k][j+k]) \
                           or (dp[k][i][j+l-k] and dp[l-k][i+k][j]):
                            dp[l][i][j] = True
                            break
        return dp[n][0][0]

s1 = ['rgtae', 'greta']
s2 = ['at', 'at']
s3 = ["pcighfdjnbwfkohtklrecxnooxyipj", "npodkfchrfpxliocgtnykhxwjbojie"]
s = s3
print(len(s[0]), s[0], s[1])
print(Solution.isScramble(Solution(), s[0], s[1]))