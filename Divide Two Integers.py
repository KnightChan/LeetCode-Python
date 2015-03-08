class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        '''
        Divide two integers without using multiplication, division and mod operator. 
        '''
        x, y = dividend, divisor
        sign = 1
        if x < 0:
            x *= -1
            sign *= -1
        if y < 0:
            y *= -1
            sign *= -1
        c, x = self.help(x, y)
        while x >= y:
            r, x = self.help(x, y)
            c += r
        return c * sign
    
    def help(self, a, b):
        if a < b:
            return [0, a]
        counter = 1
        t = b
        while a >= t + t:
            t = t + t
            counter = counter + counter
        return [counter, a - t]
