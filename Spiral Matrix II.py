class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        '''
        Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
        '''
        l, r, u, d = 0, n - 1, 0, n - 1
        m = [[0] * n for row in range(n)]
        k = 0
        while l <= r and u <= d:
            for i in range(l, r):
                k += 1
                m[u][i] = k
            for i in range(u, d + 1):
                k += 1
                m[i][r] = k
            if l == r or u == d:
                break
            for i in range(r - 1, l, -1):
                k += 1
                m[d][i] = k
            for i in range(d, u, -1):
                k += 1
                m[i][l] = k
            l += 1
            r -= 1
            u += 1
            d -= 1
        return m

n1 = 5
n = n1
print(n)
m = Solution.generateMatrix(Solution(), n)
for row in m:
    print(row)