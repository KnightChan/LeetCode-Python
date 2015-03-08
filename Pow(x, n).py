class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        '''
        Implement pow(x, n). 
        '''
        if n < 0:
            x = 1 / x
            n *= -1
        ex = 1
        base = x
        while n > 0:
            if n % 2 == 1:
                ex *= base
            n //= 2
            base *= base
        return ex

s2 = [8.88023, 3]
s1 = [2, 31]
s3 = [34.00515, -3]
s = s3
print(s)
print(Solution.pow(Solution(), s[0], s[1]))