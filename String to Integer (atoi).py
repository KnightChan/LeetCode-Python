class Solution:
    # @return an integer
    def atoi(self, str):
        '''
        Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.
Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
        '''
        s = str.strip()
        sign = 1
        flag = 0
        res = 0
        for c in s:
            if c == '+':
                if flag != 0:
                    return 0
                sign = 1
                flag = 1
            elif c == '-':
                if flag != 0:
                    return 0
                sign = -1
                flag = 1
            elif ord(c) in range(ord('0'), ord('9') + 1):
                res = res * 10 + ord(c) - ord('0')
                flag = 2
            else:
                if flag != 2:
                    return 0
                else:
                    break
        if sign == 1:
            return min(res * sign, 2147483647)
        else:
            return max(res * sign, -2147483648)

s0 = "120030221"
s = s0
print(len(s), s)
print(Solution.atoi(Solution(), s))