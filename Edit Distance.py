class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        '''
         Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
        '''
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for row in range(n1 + 1)]
        for i in range(0, n1 + 1):
            for j in range(0, n2 + 1):
                dp[i][j] = max(i, j)
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i - 1][j - 1] + 1
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] -= 1
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[n1][n2]

s1 = ['ab', 'bc']
s = s1
print(s)
print(Solution.minDistance(Solution(), s[0], s[1]))