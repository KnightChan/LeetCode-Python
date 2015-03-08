class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        '''
        Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

        '''
        if len(num) < 3:
            return target
        num.sort()
        res = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j = i + 1
            k = len(num) - 1
            while j < k:
                x = num[i] + num[j] + num[k]
                if abs(target - x) < abs(target - res):
                    res = x
                if x < target:
                    j += 1
                else:
                    k -= 1
        return res

num1 = [-1, 0, 1, 2, -1, -4]
num2 = [-1, 2, 1, -4]
num = num2
print(len(num), num)
res = Solution.threeSumClosest(Solution(), num, 1)
print(res)