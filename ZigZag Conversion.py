class Solution:
    # @return a string
    def convert(self, s, nRows):
        '''
         The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
        '''
        if nRows <= 1:
            return s
        interval = 2 * nRows - 2
        res = s[::interval]
        for i in range(1, nRows - 1):
            k = i
            x = interval - 2 * i
            while k < len(s):
                res += s[k]
                k += x
                x = interval - x
        res += s[nRows - 1::interval]
        return res

s0 = "AB"
s1 = "PAYPALISHIRING"
s = s0
print(len(s), s)
print(Solution.convert(Solution(), s, 1))