class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        '''
        Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4. 
        '''
        s = ')' + s
        sum = 0
        dp = [0] * len(s)
        maxrcount = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
                continue
            if s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
        return max(dp)
