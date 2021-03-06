# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        '''
        Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 
        '''
        i = 0
        while i < len(intervals):
            if intervals[i].end < newInterval.start or newInterval.end < intervals[i].start:
                i += 1
                continue
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            del intervals[i]
        inserted = False
        for i in range(len(intervals)):
            if intervals[i].start >= newInterval.start:
                intervals.insert(i, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)
        return intervals
