'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        merged = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if merged and interval.start <= merged[-1].end:
                if interval.end > merged[-1].end:
                    merged[-1].end = interval.end
            else:
                merged.append(interval)
        return merged


intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
res = Solution().merge(intervals)
for i in res:
    print i.start, i.end
