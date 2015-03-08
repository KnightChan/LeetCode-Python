class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        '''
        Implement int sqrt(int x).

Compute and return the square root of x.
        '''
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return l

n1 = 111
n = n1
print(n)
print(Solution.sqrt(Solution(), n))