#coding:utf-8
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        '''
        The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
        '''
        def fac(n):
            ans = 1
            for i in range(1, n + 1):
                ans *= i
            return ans
        def findMthFalse(used, m):
            for i in range(len(used)):
                if not used[i]:
                    m -= 1
                    if m == 0:
                        used[i] = True
                        return i
            return -1
        ith = 0
        used = [False] * n
        ans = ''
        nfac = fac(n)
        while ith < n:
            nfac /= n - ith
            ith += 1
            m = (k - 1) // nfac + 1
            k -= (m - 1) * nfac
            ans += chr(findMthFalse(used, m) + 1 + ord('0'))
        return ans

s1 = [3, 4]
s = s1
print(s)
print(Solution.getPermutation(Solution(), s[0], s[1]))