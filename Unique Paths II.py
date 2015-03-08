class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100.
        '''
        if len(obstacleGrid) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for row in range(m)]
        for i in range(m):
            for j in range(n):
                if i + j == 0:
                    dp[i][j] = 1 * (1 - obstacleGrid[i][j])
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j] * (1 - obstacleGrid[i][j])
                if j > 0:
                    dp[i][j] += dp[i][j - 1] * (1 - obstacleGrid[i][j])
        return dp[m - 1][n - 1]
