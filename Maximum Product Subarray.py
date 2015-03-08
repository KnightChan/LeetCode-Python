class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        ''' Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. '''
        min_positive = 0
        max_negetive = 0
        max_product = A[0]
        now_product = 1
        for a in A:
            if a == 0:
                now_product = 1
                max_negetive = 0
                min_positive = 0
                max_product = max(max_product, 0)
                continue
            now_product *= a
            max_product = max(now_product, max_product)
            if min_positive > 0:
                max_product = max(max_product, now_product // min_positive)
            if max_negetive < 0:
                max_product = max(max_product, now_product // max_negetive)
            if now_product > 0 and (min_positive == 0 or now_product < min_positive):
                min_positive = now_product
            if now_product < 0 and (max_negetive == 0 or now_product > max_negetive):
                max_negetive = now_product
        return max_product

a1 = [2, 0, 3, -1, 4]
a2 = [2,-5,-2,-4,3]
a = a2
print(a)
s = Solution()
print(s.maxProduct(a))