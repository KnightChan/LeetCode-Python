class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        '''
        Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area. 
        '''
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        height = [[0] * n for row in range(m)]
        for i in range(m):
            for j in range(n):
                k = ord(matrix[i][j]) - ord('0')
                height[i][j] = (height[i - 1][j] + 1) * k
        maximum = 0
        for i in range(m):
            maximum = max(maximum, self.largestRectangleArea(height[i]))
        return maximum

    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        '''
         Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
        '''
        n = len(height) + 1
        height.append(-1)
        stack = [[-1, -1]]
        maximum = 0
        for i in range(n):
            last = stack.pop()
            k = i
            while height[i] < last[0]:
                maximum = max(maximum, (i - last[1]) * last[0])
                k = last[1]
                last = stack.pop()
            stack.append(last)
            stack.append([height[i], k])
        return maximum
