class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        '''
        You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
        '''
        n = len(matrix)
        l = 0
        r = n
        while r - l > 1:
            for i in range(l, r - 1):
                matrix[l][i], matrix[i][r - 1], matrix[r - 1][r - 1 - i + l], matrix[r - 1 - i + l][l] = \
                matrix[r - 1 - i + l][l], matrix[l][i], matrix[i][r - 1], matrix[r - 1][r - 1 - i + l]
            l += 1
            r -= 1
        return matrix

n = 10
m = []
for i in range(n):
    m.append([i * n + j + 1 for j in range(n)])
for i in range(len(m)):
    print(m[i])
res = Solution.rotate(Solution(), m)
print()
for i in range(len(res)):
    print(res[i])
