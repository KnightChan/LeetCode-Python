#coding:utf-8
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        '''
         Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
        '''
        n = len(num)
        x = -1
        for i in range(n - 1, 0, -1):
            if num[i - 1] < num[i]:
                x = i - 1
                break
        if x == -1:
            self.reverse(num)
            return num
        y = x + 1
        for j in range(x + 1, n):
            if num[x] >= num[j]:
                y = j - 1
                break
        if num[x] < num[n - 1]:
            y = n - 1
        t = num[x]
        num[x] = num[y]
        num[y] = t
        num[x + 1:] = self.reverse(num[x + 1:])
        return num

    def reverse(self, a):
        l = 0
        r = len(a) - 1
        while l < r:
            t = a[l]
            a[l] = a[r]
            a[r] = t
            l += 1
            r -= 1
        return a

s0 = [1]
s1 = [1, 3, 2]
s2 = [2,2,7,5,4,3,2,2,1]
s = s2
print(len(s), s)
print(Solution.nextPermutation(Solution(), s))