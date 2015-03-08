class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        '''
        Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 
        '''
        if len(A) == 0:
            return 0
        l = 0
        r = len(A) - 1
        while l < r:
            while l < r and A[l] != elem:
                l += 1
            while l < r and A[r] == elem:
                r -= 1
            if l < r:
                t = A[l]
                A[l] = A[r]
                A[r] = t
                l += 1
                r -= 1
        res = r + 1
        if A[r] == elem:
            res = r
        return res
