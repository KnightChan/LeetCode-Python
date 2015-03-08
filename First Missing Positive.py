class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        '''
         Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space. 
        '''
        if len(A) == 0:
            return 1
        for i in range(len(A)):
            while 0 < A[i] < len(A) and A[i] != i + 1 and A[A[i] - 1] != A[i]:
                j = A[i] - 1
                A[i], A[j] = A[j], A[i]
        i = 0
        while i < len(A):
            if A[i] != i + 1:
                break
            i += 1
        return i + 1

a0 = [-10,-3,-100,-1000,-239,1]
a1 = [-1,4,2,1,9,10]
a2 = [1, 1]
a = a2
print(a)
print(Solution.firstMissingPositive(Solution(), a))