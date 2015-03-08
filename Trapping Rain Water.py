class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        '''
         Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
        '''
        n = len(A)
        area = 0
        maxi = -1
        maxv = -1
        for i in range(n):
            if A[i] > maxv:
                maxi = i
                maxv = A[i]
        area += self.findarea(A, maxi)
        A.reverse()
        area += self.findarea(A, n - maxi - 1)
        return area

    def findarea(self, A, maxi):
        if len(A) == 0:
            return 0
        thishigh = A[0]
        i = 0
        area = 0
        while i < maxi:
            while i < maxi and A[i] <= thishigh:
                area += thishigh - A[i]
                i += 1
            thishigh = A[i]
        return area

a0 = [0,1,0,2,1,0,1,3,2,1,2,1]
a1 = [5,2,1,2,1,5]
a = []
print(len(a), a)
print(Solution.trap(Solution(), a))