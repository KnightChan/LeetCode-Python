class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        '''
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5]. 
        '''
        if len(matrix) == 0:
            return []
        res = []
        l, r = 0, len(matrix[0]) - 1
        up, down = 0, len(matrix) - 1
        while l <= r and up <= down:
            for i in range(l, r):
                res.append(matrix[up][i])
            for i in range(up, down + 1):
                res.append(matrix[i][r])
            if l == r or up == down:
                break
            for i in range(r - 1, l, -1):
                res.append(matrix[down][i])
            for i in range(down, up, -1):
                res.append(matrix[i][l])
            l += 1
            r -= 1
            up += 1
            down -= 1
        return res

n = 4
m = []
for i in range(n):
    m.append([i * n + j + 1 for j in range(n)])
m1 = [[6,9,7]]
m2 = [[6], [9], [7]]
m = m
for i in range(len(m)):
    print(m[i])
res = Solution.spiralOrder(Solution(), m)
print(res)