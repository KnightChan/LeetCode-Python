class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        ''' Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". '''
        mlen = 0
        for word in dict:
            mlen = max(len(word), mlen)
        slen = len(s)
        dp = list(range(slen + 1))
        dp[slen] = True
        for i in range(slen - 1, -1, -1):
            dp[i] = False
            for j in range(i, min(i + mlen, slen)):
                dp[i] = dp[i] or (s[i:j + 1] in dict and dp[j + 1])
        return dp[0]

A = ['1', '2', '3', '3', '2', '1', '4', '5', '4']
a = 'abcdefg'
so = Solution()
res = so.wordBreak(a, A)
print(res)