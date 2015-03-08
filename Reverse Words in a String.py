class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        """ Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the". """
        strs = s.split(' ')
        dic = []
        for str in strs:
            dic.append(str)
        dic_rev = [str for str in dic if str != '']
        dic_rev.reverse()
        #print(dic_rev)
        res = " ".join(dic_rev).strip(' ')
        return res