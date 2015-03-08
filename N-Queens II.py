#coding:utf-8
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        '''
        Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
        '''
        def dfs(ith, n, lr, rl, ud):
            if ith == n:
                return 1
            ones = (1 << n) - 1
            count = 0
            for i in range(1, n + 1):
                k = 1 << (n - i)
                if (k & lr) + (k & rl) + (k & ud) > 0:
                    continue
                count += dfs(ith + 1, n, (lr | k) >> 1, ((rl | k) << 1) & ones, ud | k)
            return count
        return dfs(0, n, 0, 0, 0)

n1 = 12
n = n1
print(n)
res = Solution.totalNQueens(Solution(), n)
print(res)