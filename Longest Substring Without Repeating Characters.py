class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        '''
        Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
        '''
        dic = {}
        maxlen = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] > start:
                maxlen = max(maxlen, i - start)
                start = dic[s[i]]
            dic[s[i]] = i + 1
        maxlen = max(maxlen, len(s) - start)
        return maxlen

s1 = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
s2 = "aaabcabc"
s3 = "ruowzgiooobpple"
s4 = "qopubjguxhxdipfzwswybgfylqvjzhar"
s = s4
print(len(s), s)
print(Solution.lengthOfLongestSubstring(Solution(), s))