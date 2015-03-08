class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        '''
         Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.) 
        '''
        return self.on_solution(A)
        #return self.dp_solution(A)

    def on_solution(self, A):
        n = len(A)
        l = 0
        r = 1
        step = 0
        while r < n:
            nextr = -1
            for i in range(l, r):
                if A[i] + i > nextr:
                    nextr = A[i] + i
            l = r
            r = nextr + 1
            step += 1
        return step

    #TLE
    def dp_solution(self, A):
        dp = [len(A)] * len(A)
        dp[0] = 0
        for i in range(1, len(A)):
            for j in range(i - 1, -1, -1):
                if A[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[len(A) - 1]

a1 = [1,2,1,1,1]
a = a1
print(a)
print(Solution.dp_solution(Solution(), a))