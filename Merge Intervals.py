# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        '''
        Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 
        '''
        if len(intervals) == 0:
            return []
        return self.solution_sort(intervals)
        #return self.solution_discrete(intervals)

    #388ms
    def solution_sort(self, intervals):
        def intervalCmp(x, y):
            return cmp(x.start, y.start)
        intervals.sort(cmp=intervalCmp)
        l, r = intervals[0].start, intervals[0].end
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i].start <= r:
                r = max(r, intervals[i].end)
            else:
                ans.append(Interval(l, r))
                l, r = intervals[i].start, intervals[i].end
        ans.append(Interval(l, r))
        return ans

    #364ms
    def solution_discrete(self, intervals):
        allValues = []
        for iv in intervals:
            allValues.append(iv.start)
            allValues.append(iv.end)
        allValues.sort()
        valueIndexMap = {}
        indexValueList = []
        k = -1
        for i in range(len(allValues)):
            if i > 0 and allValues[i] == allValues[i - 1]:
                continue
            elif i > 0 and allValues[i] > allValues[i - 1] + 1:
                k += 1
                valueIndexMap[allValues[i - 1] + 1] = k
                indexValueList.append(allValues[i - 1] + 1)
            k += 1
            valueIndexMap[allValues[i]] = k
            indexValueList.append(allValues[i])
        #print(allValues)
        #print(indexValueList)
        #print(valueIndexMap)
        indexIntervals = []
        for iv in intervals:
            indexIntervals.append(Interval(valueIndexMap[iv.start], valueIndexMap[iv.end]))

        def solution_array(indexIntervals, n):
            cover = [0] * n
            for iv in indexIntervals:
                cover[iv.start] = max(cover[iv.start], iv.end - iv.start + 1)
            ans = []
            l, r = 0, 0
            while True:
                while l < n and cover[l] == 0:
                    l += 1
                if l == n:
                    break
                r = l
                lens = cover[l] -1
                while lens > 0:
                    r += 1
                    lens -= 1
                    if r < n:
                        lens = max(lens, cover[r] - 1)
                ans.append(Interval(l, r))
                l = r + 1
            return ans
        indexAns = solution_array(indexIntervals, len(indexValueList))
        ans = []
        for indexIv in indexAns:
            ans.append(Interval(indexValueList[indexIv.start], indexValueList[indexIv.end]))
        return ans

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]; "


s1 = [[1,3], [6,7], [2, 4]]
s2 = [[1,4], [5,6]]
s3 = [[1,4],[0,0]]
ss = s3
s = []
for iv in ss:
    s.append(Interval(iv[0], iv[1]))
print(''.join([str(i) for i in s]))
ans = Solution.merge(Solution(), s)
if ans:
    print(''.join([str(i) for i in ans]))