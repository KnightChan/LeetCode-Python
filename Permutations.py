class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        '''
         Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
        '''
        res = []
        self.dfs(num, [], res)
        return res

    def dfs(self, num, nowlist, res):
        if len(num) == 0:
            res.append(list(nowlist))
            return
        for i in range(len(num)):
            nowlist.append(num[i])
            del num[i]
            self.dfs(num, nowlist, res)
            num.insert(i, nowlist.pop())
