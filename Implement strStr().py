class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        '''
         Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack. 
        '''
        return self.kmp(haystack, needle)

    def kmp(self, s, t):
        if len(t) == 0:
            return s
        p = [-1] * len(t)
        j = -1
        for i in range(1, len(t)):
            while j >= 0 and t[j + 1] != t[i]:
                j = p[j]
            if t[j + 1] == t[i]:
                j += 1
            p[i] = j

        j = -1
        for i in range(len(s)):
            while j >= 0 and s[i] != t[j + 1]:
                j = p[j]
            if s[i] == t[j + 1]:
                j += 1
            if j == len(t) - 1:
                return s[i - j:]
        return None

s0 = ['abcabdabdedd', 'abd']
s1 = ['a', '']
s2 = ['babba', 'bbb']
s3 = ['abcddef', 'ddek']
s = s3
print(s)
print(Solution.strStr(Solution(), s[0], s[1]))