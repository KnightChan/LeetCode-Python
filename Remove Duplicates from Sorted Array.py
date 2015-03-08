class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        '''
         Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2]. 
        '''
        if len(A) == 0:
            return 0
        num = 1
        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                A[num] = A[i]
                num += 1
        return num
