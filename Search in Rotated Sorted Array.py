class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        '''
        Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
        '''
        #return self.directBS(A, target)
        return self.povitFirstBS(A, target)

    def directBS(self, A, target):
        l = 0
        r = len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] >= A[l]:
                if A[l] <= target <= A[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if A[mid] <= target <= A[r]:
                    l = mid
                else:
                    r = mid - 1
        if A[l] != target:
            l = -1
        return l

    def povitFirstBS(self, A, x):
        n = len(A)
        l = 0
        r = len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] > A[r]:
                l = mid + 1
            else:
                r = mid
        povit = l
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            rmid = (mid + povit) % n
            if A[rmid] >= x:
                r = mid
            else:
                l = mid + 1
        res = (l + povit) % n
        if A[res] != x:
            res = -1
        return res

s0 = [[3, 1], 1]
s = s0
print(s)
print(Solution.search(Solution(), s[0], s[1]))