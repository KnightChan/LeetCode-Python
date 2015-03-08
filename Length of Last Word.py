class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        '''
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5. 
        '''
        n = len(s) - 1
        lens = 0
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            lens += 1
            n -= 1
        return lens


