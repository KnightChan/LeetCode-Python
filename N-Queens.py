#coding:utf-8
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        '''
        The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
        '''
        def dfs(ith, n, lr, rl, ud, now, res):
            if ith == n:
                so = []
                for i in range(n):
                    s = ''
                    for j in range(n):
                        if j == now[i] - 1:
                            s += 'Q'
                        else:
                            s += '.'
                    so.append(s)
                res.append(so)
                return
            ones = (1 << n) - 1
            for i in range(1, n + 1):
                k = 1 << (n - i)
                if (k & lr) + (k & rl) + (k & ud) > 0:
                    continue
                now.append(i)
                dfs(ith + 1, n, (lr | k) >> 1, ((rl | k) << 1) & ones, ud | k, now, res)
                now.pop()
        res = []
        dfs(0, n, 0, 0, 0, [], res)
        return res

n1 = 6
n = n1
print(n)
res = Solution.solveNQueens(Solution(), n)
for so in res:
    for s in so:
        print(s)
    print('')