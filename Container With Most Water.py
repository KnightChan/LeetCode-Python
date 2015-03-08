class Solution:
    # @return an integer
    def maxArea(self, height):
        '''
        Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container. 
        '''
        marea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            t = height[l]
            if height[l] < height[r]:
                l += 1
            else:
                t = height[r]
                r -= 1
            marea = max(marea, t * (r - l + 1))
        return marea
