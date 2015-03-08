class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        '''
         Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100". 
        '''
        ia = list(reversed([ord(c) - ord('0') for c in a]))
        ib = list(reversed([ord(c) - ord('0') for c in b]))
        ic = [0] * (max(len(ia), len(ib)) + 1)
        x = 0
        for i in range(len(ic)):
            ic[i] = x
            if i < len(ia):
                ic[i] += ia[i]
            if i < len(ib):
                ic[i] += ib[i]
            x = ic[i] // 2
            ic[i] %= 2
        while len(ic) > 1 and ic[len(ic) - 1] == 0:
            ic.pop()
        return ''.join(list(reversed([chr(x + ord('0')) for x in ic])))

a1 = ['101011', '1']
a2 = ['1', '1']
a = a2
print(a[0])
print(a[1])
print(Solution.addBinary(Solution(), a[0], a[1]))