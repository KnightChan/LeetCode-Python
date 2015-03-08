class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        '''There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
        '''
        la = len(A)
        lb = len(B)
        l = la + lb
        if l % 2 == 1:
            return self.findKth(A, la, B, lb, l // 2 + 1)
        else:
            return (self.findKth(A, la, B, lb, l // 2) + self.findKth(A, la, B, lb, l // 2 + 1)) * 0.5
        return self.findMedian(A, la, B, lb)

    def findKth(self, A, la, B, lb, k):
        if la == 0:
            return B[k - 1]
        if lb == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        i = min(k // 2, la)
        j = min(k // 2, lb)
        if A[i - 1] > B[j - 1]:
            return self.findKth(A, la, B[j:], lb - j, k - j)
        else:
            return self.findKth(A[i:], la - i, B, lb, k - i)

A = [0, 10]
B = [1.1, 2.1, 3.2]
x = [[], [2,3]]
so = Solution()
print(x)
print(so.findMedianSortedArrays(x[0], x[1]))