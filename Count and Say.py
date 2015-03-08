class Solution:
    # @return a string
    def countAndSay(self, n):
        '''
        The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 
        '''
        s = '1'
        if n == 1:
            return s

        for i in range(n - 1):
            k = 1
            next = ''
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    k += 1
                else:
                    next += chr(k + ord('0')) + s[i - 1]
                    k = 1
            next += chr(k + ord('0')) + s[len(s) - 1]
            s = next
        return s

for i in range(10):
    print(Solution.countAndSay(Solution(), i))