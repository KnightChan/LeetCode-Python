class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        ''' Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''
        n = len(s)
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
        cuts = list(range(n + 1))
        cuts[n] = []
        for i in range(n - 1, -1, -1):
            cuts[i] = []
            for j in range(i, n):
                if is_palindrome[i][j]:
                    cuts[i].append(j + 1)
        reslist = []
        self.dfs(s, reslist, cuts, [], 0, n)
        return reslist

    def dfs(self, s, reslist, cuts, curres, pos, n):
        if pos == n:
            reslist.append(list(curres))
            return
        for nextpos in cuts[pos]:
            curres.append(s[pos:nextpos])
            self.dfs(s, reslist, cuts, curres, nextpos, n)
            curres.pop()

s = ''
print(len(s))
print(s)
print(Solution.partition(Solution(), s))