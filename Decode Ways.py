class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        '''
         A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
        '''
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        code = 0
        for i in range(1, len(s) + 1):
            code = (code * 10 + ord(s[i - 1]) - ord('0')) % 100
            if code % 10 > 0:
                dp[i] = dp[i - 1]
            if 10 <= code <= 26 and i > 1:
                dp[i] += dp[i - 2]
        return dp[len(s)]

s1 = '01'
s = s1
print(len(s), s)
print(Solution.numDecodings(Solution(), s))
