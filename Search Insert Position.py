#coding: utf-8
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        '''
        Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0 
        '''
        if len(A) == 0:
            return -1
        if target <= A[0]:
            return 0
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                if mid > 0 and A[mid - 1] == target:
                    r = mid - 1
                else:
                    return mid
            elif A[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l