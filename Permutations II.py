class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        '''
         Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]. 
        '''
        def nextPermutation(a):
            k = len(a) - 1
            while k > 0 and a[k - 1] >= a[k]:
                k -= 1
            i = k - 1
            if i == -1:
                return False
            while k < len(a) and a[k] > a[i]:
                k += 1
            k -= 1
            a[i], a[k] = a[k], a[i]
            a[i + 1:] = reversed(a[i + 1:])
            return True

        num.sort()
        res = [list(num)]
        while nextPermutation(num):
            res.append(list(num))
        return res

a1 = [1, 2, 3]
a = a1
print(a)
print(Solution.permuteUnique(Solution(), a))