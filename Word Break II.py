class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        ''' Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]. '''
        mlen = 0
        for word in dict:
            mlen = max(len(word), mlen)
        slen = len(s)
        dp = list(range(slen + 1))
        dp[slen] = [slen]
        for i in range(slen - 1, -1, -1):
            dp[i] = []
            for j in range(i, min(i + mlen, slen)):
                if s[i:j + 1] in dict and len(dp[j + 1]) > 0:
                    dp[i].append(j + 1)
        res = []
        if len(dp[0]) == 0:
            return res
        self.dfs(s, dp, 0, slen, [], res)
        return res

    def dfs(self, s, dp, cur, n, curpos, res):
        if cur == n:
            s1 = s
            nowplus = 0
            for pos in curpos:
                if pos != 0 and pos != n:
                    s1 = s1[:pos + nowplus] + ' ' + s1[pos + nowplus:]
                    nowplus += 1
            res.append(s1)
            return
        for pos in dp[cur]:
            curpos.append(pos)
            self.dfs(s, dp, pos, n, curpos, res)
            curpos.pop()

A = ['1', '2', '3', '3', '2', '1', '4', '5', '4']
dict = ["cat", "cats", "and", "sand", "dog"]
a = 'catsanddog'
so = Solution()
res = so.wordBreak(a, dict)
print(res)