class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        '''
         Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()" 
        '''
        res = []
        self.dfs(n, 0, '', res)
        return res
    
    def dfs(self, x, y, now, res):
        if x + y == 0:
            res.append(now)
            return
        if x > 0:
            self.dfs(x - 1, y + 1, now + '(', res)
        if y > 0:
            self.dfs(x, y - 1, now + ')', res)
