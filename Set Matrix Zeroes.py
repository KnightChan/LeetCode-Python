class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        '''
         Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
        '''
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        row1zero = 1
        col1zero = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i * j == 0:
                        if i == 0:
                            row1zero = 0
                        if j == 0:
                            col1zero = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] * matrix[i][0] == 0:
                    matrix[i][j] = 0
        for i in range(n):
            matrix[0][i] *= row1zero
        for i in range(m):
            matrix[i][0] *= col1zero
