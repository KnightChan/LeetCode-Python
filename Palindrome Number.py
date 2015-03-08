class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        '''
        Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

        '''
        t = x
        if x < 0:
            return False
        l = 0
        while t > 0:
            t //= 10
            l += 1
        for i in range(l // 2):
            a = (x // pow(10, i)) % 10
            b = (x // pow(10, l - i - 1)) % 10
            if a != b:
                return False
        return True

s0 = 120030221
s = s0
print(s)
print(Solution.isPalindrome(Solution(), s))