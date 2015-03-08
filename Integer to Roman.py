class Solution:
    # @return a string
    def intToRoman(self, num):
        '''
        Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
        '''
        dic = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100],
               ["XC", 90], ["L", 50], ["XL", 40], ["X", 10],
               ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        s = ""
        index = 0
        while num > 0:
            while num >= dic[index][1]:
                s += dic[index][0]
                num -= dic[index][1]
            index += 1
        return s
