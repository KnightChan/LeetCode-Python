class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        '''
        Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
        '''
        for i in range(m - 1, -1, -1):
            A[i + n] = A[i]
        l1, r1 = n, m + n
        l2, r2 = 0, n
        l = 0
        while l1 < r1 and l2 < r2:
            if A[l1] < B[l2]:
                A[l] = A[l1]
                l1 += 1
            else:
                A[l] = B[l2]
                l2 += 1
            l += 1
        if l1 == r1:
            for i in range(l2, r2):
                A[l] = B[i]
                l += 1

a1 = [[1, 0], [2]]
a = a1
print(a[0])
print(a[1])
print(Solution.merge(Solution(), a[0], 1, a[1], len(a[1])))
print(a[0])