#coding=utf-8
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        """
        Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
        """
        n = len(s)
        m = len(p)
        match = [[False] * (m + 1) for row in range(n + 1)]
        match[0][0] = True
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i > 0 or j > 0:
                    match[i][j] = (i >= 1 and j >= 1 and match[i - 1][j - 1] and self.matchSingle(s[i - 1], p[j - 1])) \
                                or (i >= 1 and j >= 2 and match[i - 1][j] and p[j - 1] == '*' and self.matchSingle(s[i - 1], p[j - 2])) \
                                or (j >= 1 and match[i][j - 1] and p[j - 1] == '*') \
                                or (j >= 2 and match[i][j - 2] and p[j - 1] == '*')
                    #print(i, j, s[:i], p[:j], match[i][j])
        return match[n][m]

    def matchSingle(self, s1, s2):
        return s1 == s2 or s2 == '.'

s1 = ["aaa", ".*"]
s2 = ["aab", "c*a*b"]
s = s2
print(s)
print(Solution.isMatch(Solution(), s[0], s[1]))