class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        '''
         Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3]. 
        '''
        if len(A) <= 1:
            return len(A)
        count = 1
        i = 1
        while i < len(A):
            if A[i] == A[i - 1]:
                count += 1
                if count > 2:
                    del A[i]
                    continue
                i += 1
            else:
                count = 1
                i += 1
        return len(A)