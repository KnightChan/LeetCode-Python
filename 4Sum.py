class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        '''
        Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
        '''
        n = len(num)
        num.sort()
        twoSumDic = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = num[i] + num[j]
                if x not in twoSumDic:
                    twoSumDic[x] = []
                twoSumDic[x].append([num[i], num[j], i, j])
        resSet = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = target - (num[i] + num[j])
                if x in twoSumDic:
                    for y in twoSumDic[x]:
                        if y[3] == i or y[3] == j or y[2] == i or y[2] == j:
                            continue
                        a = [num[i], num[j], y[0], y[1]]
                        a.sort()
                        resSet.add((a[0], a[1], a[2], a[3]))
        res = []
        for a in resSet:
            res.append([a[i] for i in range(len(a))])
        return res

s0 = [0, [1, 0, -1, 0, -2, 2]]
s = s0
print(Solution.fourSum(Solution(), s[1], s[0]))