class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ''' Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? '''
        ones = 0
        twos = 0
        for a in A:
            threes = twos & a
            twos = (twos | (ones & a)) & ~threes
            ones = (ones | a) & ~threes & ~twos
        return ones

    def singleNumber1(self, A):
        xbits = [1]
        bcounts = [0]
        l = 0
        for i in range(1, 32):
            xbits.append(xbits[l] << 1)
            bcounts.append(0)
            l += 1
        for a in A:
            while a > xbits[l]:
                xbits.append(xbits[l] << 1)
                bcounts.append(0)
                l += 1
        for a in A:
            for i in range(0, l + 1):
                bcounts[i] += (a & xbits[i]) >> i
        res = 0
        for i in range(0, 31):
            res += bcounts[i] % 3 * xbits[i]
        return res - bcounts[31] % 3 * xbits[31]

A = [1, 2, 3, 3, 2, 1, 4, 5, 4, 1, 2, 3, 4, 6, 5, 5]
A1 = [1, 1, 2, 1, 2, 2, 99]
A2 = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
so = Solution()
res = so.singleNumber1(A2)
print(res)