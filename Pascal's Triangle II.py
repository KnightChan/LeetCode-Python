class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        '''Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
        rowIndex += 1
        if rowIndex == 0:
            return []
        ithrow = [0] * rowIndex
        for i in range(0, rowIndex):
            ithrow[i] = 1
            for j in range(i - 1, -1, -1):
                x = ithrow[j]
                if j > 0:
                    x += ithrow[j - 1]
                ithrow[j] = x
        return ithrow

num = 2
for i in range(10):
    print(Solution.getRow(Solution(), i))