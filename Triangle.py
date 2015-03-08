class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        '''Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. '''
        n = len(triangle)
        f = [0] * (n + 1)
        dir = 0
        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                f[j] = triangle[i][j] + min(f[j + 1], f[j])
        return f[0]

t1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
t2 = [[-1],[-2,-3]]
t3 = [[-1],[3,2],[-3,1,-1]]
t = t3
print(t)
print(Solution.minimumTotal(Solution(), t))