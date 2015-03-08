class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        ''' Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. '''
        n = len(s)
        if n <= 1:
            return 0
        is_palindrome = [[False] * n for row in range(n)]
        for pos in range(0, n):
            l = 0
            while pos - l >= 0 and pos + l <= n - 1 and s[pos - l] == s[pos + l]:
                is_palindrome[pos - l][pos + l] = True
                l += 1
            l = 0
            while pos - l - 1 >= 0 and pos + l <= n - 1 and s[pos - l - 1] == s[pos + l]:
                is_palindrome[pos - l - 1][pos + l] = True
                l += 1
        min_cut = list(range(n + 1))
        min_cut[n] = 0
        for i in range(n - 1, -1, -1):
            min_cut[i] = n
            for j in range(i, n):
                if is_palindrome[i][j]:
                    min_cut[i] = min(min_cut[i], min_cut[j + 1] + 1)
        return min_cut[0] - 1

s='aab'
print(len(s))
print(s)
print(Solution.minCut(Solution(), s))