'''
Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start
times.

Example 1:
    Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
    Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
    [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, new):
        """
        :type intervals: List[Interval]
        :type new: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [new]
        merged = []
        count = 0
        for interval in intervals:
            if new.start > interval.end:            # Insert intervals before
                merged.append(interval)
            elif new.end >= interval.start:         # Modify intervals
                new.start = min(new.start, interval.start)
                new.end = max(new.end, interval.end)
            else:                                   
                break
            count += 1
        merged.append(new)                          # Insert new interval 
        for i in xrange(count, len(intervals)):     # Insert remaining
            merged.append(intervals[i])
        return merged

intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), 
            Interval(8, 10), Interval(12, 16), Interval(17, 20)]
ret = Solution().insert(intervals, Interval(4, 9))
for i in ret:
    print i.start, i.end
