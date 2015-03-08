class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        '''Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            ithrow = []
            for j in range(i + 1):
                x = 0
                if j < i:
                    x = res[i - 1][j]
                if j > 0:
                    x += res[i - 1][j - 1]
                ithrow.append(x)
            res.append(ithrow)
        return res

num = 10
print(Solution.generate(Solution(), num))