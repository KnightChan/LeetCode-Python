class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        '''
        Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want. 
        '''
        dig2charDic = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        self.dfs(digits, "", dig2charDic, res)
        return res

    def dfs(self, digits, chars, dig2charDic, res):
        if digits == "":
            res.append(chars)
            return
        for c in dig2charDic[digits[0]]:
            self.dfs(digits[1:], chars + c, dig2charDic, res)

d0 = "23"
d = d0
print(d)
print(Solution.letterCombinations(Solution(), d))