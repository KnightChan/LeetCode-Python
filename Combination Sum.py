class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        '''
         Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3] 
        '''
        p = [set() for i in range(target + 1)]
        f = [False] * (target + 1)
        last_no = [-1] * (target + 1)
        f[0] = True
        candidates.sort(reverse=True)
        for i in range(len(candidates)):
            for j in range(candidates[i], target + 1):
                if f[j - candidates[i]] and i >= last_no[j - candidates[i]]:
                    f[j] = True
                    p[j].add(j - candidates[i])
                    last_no[j] = i
        res = []
        self.path_dfs(p, target, [], res)
        return res

    def path_dfs(self, path, v, nowlist, res):
        if v == 0:
            res.append(list(nowlist))
            return
        for par in path[v]:
            if len(nowlist) > 0 and v - par < nowlist[len(nowlist) - 1]:
                continue
            nowlist.append(v - par)
            self.path_dfs(path, par, nowlist, res)
            nowlist.pop()

a0 = [10, [2, 3, 6, 7]]
a1 = [8, [10, 1, 2, 7, 6, 1, 5]]
a = a1
print(a)
print(Solution.combinationSum(Solution(), a[1], a[0]))