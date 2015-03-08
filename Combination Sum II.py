class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        '''
          Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
        '''
        res = self.use_dp(candidates, target)
        return res

        #candidates.sort()
        #res = []
        #self.dfs(candidates, 0, target, [], res)
        #return res

    #TLE
    def dfs(self, candidates, i, v, nowlist, res):
        if v == 0:
            res.append(list(nowlist))
            return
        if v < 0:
            return
        for start in range(i, len(candidates)):
            nowlist.append(candidates[start])
            self.dfs(candidates, start + 1, v - candidates[start], nowlist, res)
            nowlist.pop()
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1

    def use_dp(self, candidates, target):
        p = [set() for i in range(target + 1)]
        f = [False] * (target + 1)
        f[0] = True
        candidates.sort(reverse=True)
        dic_count = {}
        for i in range(len(candidates)):
            if candidates[i] not in dic_count:
                dic_count[candidates[i]] = 0
            dic_count[candidates[i]] += 1
            for j in range(target, candidates[i] - 1, -1):
                if f[j - candidates[i]]:
                    f[j] = True
                    p[j].add(j - candidates[i])
        res = []
        self.path_dfs(dic_count, p, target, [], res)
        return res

    def path_dfs(self, dic_count, path, v, nowlist, res):
        if v == 0:
            res.append(list(nowlist))
            return
        for par in path[v]:
            if dic_count[v - par] == 0 or (len(nowlist) > 0 and v - par < nowlist[len(nowlist) - 1]):
                continue
            nowlist.append(v - par)
            dic_count[v - par] -= 1
            self.path_dfs(dic_count, path, par, nowlist, res)
            dic_count[v - par] += 1
            nowlist.pop()


a0 = [10, [2, 3, 6, 7]]
a1 = [12, [10, 1, 2, 7, 6, 1, 5]]
a = a1
print(a)
print(Solution.combinationSum2(Solution(), a[1], a[0]))