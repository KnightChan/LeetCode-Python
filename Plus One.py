class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        '''
        Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
        '''
        if len(digits) == 0:
            res = [1]
            return res
        digits.reverse()
        res = digits
        res[0] += 1
        i = 0
        while i < len(res) and res[i] > 9:
            res[i] -= 10
            if i < len(res) - 1:
                res[i + 1] += 1
            else:
                res.append(1)
                break
            i += 1
        res.reverse()
        return res

print(Solution.plusOne(Solution(), [0, 1]))