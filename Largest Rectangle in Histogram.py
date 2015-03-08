class Solution:
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

a1 = []
a2 = [2,1,5,6,2,3]
a3 = [2,1,2]
a = a3
print(len(a), a)
print(Solution.largestRectangleArea(Solution(), a))