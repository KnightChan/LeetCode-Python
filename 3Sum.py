#coding=utf-8
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        '''
        Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
        '''
        num.sort()
        resset = set()
        for i in range(len(num) - 2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            j = i + 1
            k = len(num) - 1
            while j < k:
                x = num[i] + num[j] + num[k]
                if x == 0:
                    resset.add((num[i], num[j], num[k]))
                    j += 1
                    k -= 1
                elif x < 0:
                    j += 1
                else:
                    k -= 1
        res = []
        for item in resset:
            res.append([item[0], item[1], item[2]])
        return res

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum_withDic(self, num):
        '''
        Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
        '''
        num.sort()
        dic = {}
        res = []
        for i in range(len(num)):
            dic[num[i]] = i
        for i in range(len(num) - 2):
            if i > 0 and num[i] == num[i - 1]:
                continue
            for j in range(i + 1, len(num) - 1):
                if j > i + 1 and num[j] == num[j - 1]:
                    continue
                kv = -num[i] - num[j]
                if kv in dic and dic[kv] > j:
                    if len(res) > 0:
                        x = res.pop()
                        res.append(x)
                        if x[0] == num[i] and x[1] == num[j] and x[2] == kv:
                            continue
                    res.append([num[i], num[j], kv])
        return res

num1 = [-1, 0, 1, 2, -1, -4]
num = num1
print(len(num), num)
res = Solution.threeSum(Solution(), num)
print(len(res), res)