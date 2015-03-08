class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        '''
        Write a function to find the longest common prefix string amongst an array of strings. 
        '''
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        lens = 0
        maxlen = len(strs[0])
        for str in strs:
            maxlen = min(maxlen, len(str))
        for lens in range(maxlen):
            for str in strs:
                if str[lens] != strs[0][lens]:
                    return strs[0][0:lens]
        return strs[0][0:maxlen]
