class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        '''
         Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 
        '''
        return self.on_solution(A)

    def on_solution(self, A):
        n = len(A)
        l = 0
        r = 1
        step = 0
        while r > l and r < n:
            nextr = -1
            for i in range(l, r):
                if A[i] + i > nextr:
                    nextr = A[i] + i
            l = r
            r = nextr + 1
            step += 1
        return r >= n
