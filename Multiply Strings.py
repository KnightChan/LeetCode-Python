class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        '''
        Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
        '''
        a = [ord(c) - ord('0') for c in num1]
        a.reverse()
        b = [ord(c) - ord('0') for c in num2]
        b.reverse()
        c = [0] * (len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                c[i + j] += a[i] * b[j]
        for i in range(len(a) + len(b) - 1):
            c[i + 1] += c[i] // 10
            c[i] %= 10
        while len(c) > 1 and c[len(c) - 1] == 0:
            c.pop()
        c.reverse()
        return ''.join([chr(i + ord('0')) for i in c])

num1 = ['1234567890', '9876543210']
num = num1
print(num)
print(Solution.multiply(Solution(), num[0], num[1]))