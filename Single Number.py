class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        '''Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? '''
        res = 0
        for a in A:
            res = res ^ a
        return res

A = [1, 2, 3, 3, 2, 1, 4, 5, 4]
so = Solution()
res = so.singleNumber(A)
print(res)