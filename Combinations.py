class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        '''
         Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

        '''
        res = []
        self.dfs(n, k, 0, 0, [], res)
        return res
    
    def dfs(self, n, k, ith, x, nowlist, res):
        if ith == k:
            res.append(list(nowlist))
            return
        for v in range(x + 1, n + 1):
            nowlist.append(v)
            self.dfs(n, k, ith + 1, v, nowlist, res)
            nowlist.pop()
