class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        '''
        Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 
        '''
        if len(A) < 1 or A[0] > target or A[len(A) - 1] < target:
            return [-1, -1]
        
        lb = self.searchLeftBound(A, target)
        rb = self.searchRightBound(A, target)
        return [lb, rb]
        
    def searchLeftBound(self, A, target):
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                if mid == 0:
                    return mid
                if A[mid - 1] == target:
                    r = mid - 1
                else:
                    return mid
            elif A[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    
    def searchRightBound(self, A, target):
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                if mid == len(A) - 1:
                    return mid
                if A[mid + 1] == target:
                    l = mid + 1
                else:
                    return mid
            elif A[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1