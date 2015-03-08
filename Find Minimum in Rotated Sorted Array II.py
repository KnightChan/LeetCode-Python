class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        '''
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
        '''
        l, r = 0, len(num) - 1
        while l < r:
            mid = (l + r) // 2
            if num[mid] == num[r]:
                r -= 1
                continue
            if num[mid] < num[r]:
                r = mid
            else:
                l = mid + 1
        return num[l]

a1 = [1, 1, 2, 0, 1, 1]
a2 = [1, 3, 3]
a = a2
print(len(a), a)
print(Solution.findMin(Solution(), a))