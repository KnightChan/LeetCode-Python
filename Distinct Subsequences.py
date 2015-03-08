class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ''' Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3. '''
        f = [[0] * (len(T) + 1) for row in range(len(S) + 1)]
        for i in range(0, len(S)):
            f[i][0] = 1
        for i in range(1, len(S) + 1):
            for j in range(1, len(T) + 1):
                f[i][j] = f[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    f[i][j] += f[i - 1][j - 1]
        return f[len(S)][len(T)]

S1 = ["raabbbit", "rabbit"]
S = S1
print(S)
print(Solution.numDistinct(Solution(), S[0], S[1]))