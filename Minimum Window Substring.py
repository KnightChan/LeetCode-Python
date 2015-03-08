class Solution:
    # @return a string
    def minWindow(self, S, T):
        '''
         Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S. 
        '''
        if T == '':
            return ''
        countT = {}
        for c in T:
            if c not in countT:
                countT[c] = 0
            countT[c] += 1
        n = len(countT)
        countLR = {}
        for c in countT:
            countLR[c] = 0
        l, r = 0, 0
        min_count = len(S) + 1
        min_window = ''
        while True:
            while n > 0 and r < len(S):
                if S[r] in countLR:
                    countLR[S[r]] += 1
                    if countLR[S[r]] == countT[S[r]]:
                        n -= 1
                r += 1
            if n != 0:
                break
            while n == 0:
                if S[l] in countLR:
                    countLR[S[l]] -= 1
                    if countLR[S[l]] == countT[S[l]] - 1:
                        n += 1
                l += 1
            if r - l + 1 < min_count:
                min_window = S[l - 1:r]
                min_count = r - l + 1
        return min_window

s1 = ["ADOBECODEBANC", "ABC"]
s2 = ['aa', 'aa']
s = s2
print(s)
print(Solution.minWindow(Solution(), s[0], s[1]))

