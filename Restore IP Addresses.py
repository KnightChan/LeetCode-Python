class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        '''
        Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
        '''
        def dfs(s, str, n, now, res):
            if len(str) == 4\
                or (len(str) == 3 and str > '255')\
                or (len(str) > 1 and str[0] == '0')\
                or (s == '' and n != 3)\
                or (n > 3):
                return
            if s == '':
                res.append(now[1:] + '.' + str)
                return
            dfs(s[1:], str + s[0], n, now, res)
            if str != '':
                dfs(s[1:], s[0], n + 1, now + '.' + str, res)
        res = []
        dfs(s, '', 0, '', res)
        return res

s1 = '25525511135'
s2 = "010010"
s3 = '111111111111111111111111111111111111111111111111111111111111111111111111111111'
s = s3
print(s)
print(Solution.restoreIpAddresses(Solution(), s))