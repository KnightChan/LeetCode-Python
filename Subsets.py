class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        '''
         Given a set of distinct integers, S, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
        '''
        S.sort()
        def dfs(a, now, res):
            res.append(list(now))
            if len(a) == 0:
                return
            for i in range(len(a)):
                if i > 0 and a[i] == a[i - 1]:
                    continue
                now.append(a[i])
                dfs(a[i + 1:], now, res)
                now.pop()
        res = []
        dfs(S, [], res)
        return res

a1 = [1, 2, 2]
a2 = [1, 2, 3]
a = a2
print(len(a), a)
print(Solution.subsets(Solution(), a))