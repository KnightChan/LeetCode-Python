class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        '''
        Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
        '''
        hashTable = {}
        for s in strs:
            sorted_s = sorted(s)
            ss = ''.join(sorted_s)
            if ss not in hashTable:
                hashTable[ss] = []
            hashTable[ss].append(s)

        res = []
        for s in hashTable:
            if len(hashTable[s]) > 1:
                res += [os for os in hashTable[s]]
        return res

s1 = ['cbad']
s = s1
print(s)
print(Solution.anagrams(Solution(), s))