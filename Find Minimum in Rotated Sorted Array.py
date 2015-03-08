class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        '''
        Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
        '''
        l = 0
        r = len(num) - 1
        while l < r:
            mid = (l + r) // 2
            if num[mid] < num[r]:
                r = mid
            else:
                l = mid + 1
        return num[l]
