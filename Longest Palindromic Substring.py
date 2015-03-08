class Solution:
    # @return a string
    def longestPalindrome(self, s):
        '''
        Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
        '''
        if s == s[::-1]:
            return s
        last = -1
        lens = 0
        for i in range(2):
            l = i
            r = len(s)
            if r % 2 == 1 - i:
                r -= 1
            while l < r:
                mid = (l + r) // 2
                if mid % 2 == 1 - i:
                    mid += 1
                start = self.checkPalindromic(s, mid)
                #print(l, r, mid, start)
                if start != -1:
                    l = mid
                    if mid > lens:
                        lens = mid
                        last = start
                else:
                    r = mid - 2
        return s[last:last + lens]

    def checkPalindromic(self, s, l):
        for i in range(len(s) - l + 1):
            if s[i:i + l] == s[i:i + l][::-1]:
                return i
        return -1

s0 = "abcddcba"
s1 = "abadd"
s = s1
print(len(s), s)
print(Solution.longestPalindrome(Solution(), s))