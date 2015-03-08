class Solution:
    # @return an integer
    def romanToInt(self, s):
        '''
        Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
        '''
        dic = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100],
               ["XC", 90], ["L", 50], ["XL", 40], ["X", 10],
               ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        index = 0
        t = 0
        num = 0
        while index < len(dic) and t < len(s):
            while s[t:t + len(dic[index][0])] == dic[index][0]:
                num += dic[index][1]
                t += len(dic[index][0])
            index += 1
        return num
