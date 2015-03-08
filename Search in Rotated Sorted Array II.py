class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        '''
        Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
        '''
        l, r = 0, len(A) - 1
        while l <= r:
            if l == r:
                return target == A[l]
            mid = (l + r) // 2
            if A[mid] == target:
                return True
            if A[mid] == A[r]:
                r -= 1
                continue
            if A[mid] > A[r]:
                if A[l] <= target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if A[mid] < target <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

a1 = [0, [1, 3]]
a = a1
print(a[0], a[1])
print(Solution.search(Solution(), a[1], a[0]))